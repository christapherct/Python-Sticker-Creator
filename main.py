from segment import Segment

text = "Eppo"
seg = Segment("images/image.jpg", text)
seg_map = seg.find_segments()
seg.vis_segmentation()
