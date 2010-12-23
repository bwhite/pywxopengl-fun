"""
  This script is meant to be run several times, from IPython.
  Modify whatever you like in it, but sure to think of your globals() as
  being preserved in between
"""
from camerawindow import CameraWindow
from OpenGL.GL import *

if not 'window' in globals():
  window = CameraWindow()
  color = []
  xyz = []
  point_size = 2


def scatter():
  global color, xyz
  xyz = np.random.rand(1000, 3) - 0.5
  color = np.random.rand(1000, 3)
  window.Refresh()


@window.event
def on_draw_axes():
  global color, xyz
  """
  # The name on_draw_axes should be deprecated. Really it's just a
  # 'user settable' callback for drawing in the camera window (after the
  # projection matrices are initialized, etc)
  """
  # Draw the points
  glPointSize(point_size)
  glEnableClientState(GL_VERTEX_ARRAY)
  glVertexPointerf(xyz)

  if not color is None:
   glEnableClientState(GL_COLOR_ARRAY)
   glColorPointerf(color)
   glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
   glEnable(GL_BLEND)
  glColor3f(1,1,1)
  glDrawElementsui(GL_POINTS, np.array(range(len(xyz))))
  glDisableClientState(GL_COLOR_ARRAY)
  glDisableClientState(GL_VERTEX_ARRAY)
  glDisable(GL_BLEND)
