[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/X3WkcXtG)
# Week 3 - Train a LoRA model and generate some images.  
本次作業主要是按照[Stable Diffusion -- 訓練LoRA](https://vocus.cc/article/642db062fd897800014596ad)系列完成的  
  
## 資料準備  
* 首先需要選擇想要訓練的照片，我使用了`阿甘妙世界`的角色作為訓練資料的圖片  
* 透過[BIRME](https://www.birme.net/?target_width=512&target_height=512)剪裁照片(把過大的尺寸裁切成512x512的訓練素材圖)  
* 在雲端內創資料夾，並將剪裁好的相片放入名為dataset的資料夾中  
  其檔案夾路徑為`Loras - animate(自己創一個這的專案的名稱) - datast`  
* 執行[Dataset Maker](https://colab.research.google.com/github/hollowstrawberry/kohya-colab/blob/main/Dataset_Maker.ipynb)的第一步驟(連接資料夾到剛剛創建的dataset)與第四步驟(生成提示詞)  
  
## LoRA訓練  
* 根據[Lora Trainer](https://colab.research.google.com/drive/1DOXzROm1Sz-rcwgdOoCCX3UdrEbIippX#scrollTo=rmCPmqFL6hCQ)給的空格填入需求，相關參數在`report.pdf`中  
* 若是要用wandb監測數據的話，需要在載入相關資料後找到`train_network.py`與`train_network_wrapper.py`兩個檔並加入相關程式碼(如提供之檔案所示)  
* 訓練結束後會產生`animate-20.safetensors`檔，其路徑在`Loras - animate(自己創一個這的專案的名稱) - output`  
  
## 將LoRA模型加入Stable Diffusion  
* 這邊是參考了[AI繪圖-四分鐘四個步驟!簡易快速安裝單機版stable-diffusion-webui(AUTOMATIC1111)](https://vocus.cc/article/63f87151fd89780001283144)來安裝stable-diffusion-webui
* 首先輸入以下指令安裝stable-diffusion-webui  
  ```  
  git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git  
  ```  
* 安裝若是沒有問題，點擊`"stable-diffusion-webui\webui-user.bat"`
* 若是出現`AssertionError: Torch is not able to use GPU; add --skip-torch-cuda-test to COMMANDLINE_ARGS variable to disable this check`相關問題，請右鍵點擊webui-user.bat開啟記事本編輯，並在`set COMMANDLINE_ARGS=`後加入這一句話
  ```  
  set COMMANDLINE_ARGS= --lowvram --precision full --no-half --skip-torch-cuda-test  
  ```  
