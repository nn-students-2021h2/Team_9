* LaTex renderer:
    * Bot takes LaTex equation and returns image with rendered equation
    * If equation is incorrect, bot sends message from LaTex compiler
* OpenVINO inference
    * Bot uses OpenVINO to make inference with user's images
    * Bot allows to choose task (classification or detection), model (from OpenModelZoo)
    * Bor returns inference result for user's image
    * Can be helpful, if you need quick inference with few pictures, but you don't have PC with OpenVINO installed around