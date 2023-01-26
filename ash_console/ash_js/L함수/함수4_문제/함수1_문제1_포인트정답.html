<script>
    /*
      아래  userData는 회원번호와이름이고 , 
      pointData는 포인트와 회원번호이다.
      포인트는 여러번쌓을수있고, 전부 누적해서 합을 구한다.

      [문제]
        회원별로 포인터 점수를 합산한표를 그리고,
        포인터 점수가 가장높은 회원의 이름을 출력하시오.
        
      [정답]
        이만수 (3점으로1002번이 가장높으므로 정답)
    */

    function getSplitArr(doubleStr){
      var tempListStr = doubleStr.split(",");
      var arr = [];
      for(var i = 0; i < tempListStr.length;i++){
        var tempStr = tempListStr[i].split("/");
        arr[i] = [];
        arr[i][0] = tempStr[0];
        arr[i][1] = tempStr[1];
      }
      return arr;
    }
    function getMaxUser(userPointArr, ){
      var max = userPointArr[0][2];
      var name = userPointArr[0][1];
      for(var i = 0; i < userPointArr.length; i++){
        if(max < userPointArr[i][2]){
          max = userPointArr[i][2];
          name = userPointArr[i][1];
        }
      }
      return name;
    }   
    function printTable(userPointArr){
      for(var i = 0; i < userPointArr.length; i++){
        
        console.log(userPointArr[i][0] + " " + userPointArr[i][1] + " " +userPointArr[i][2] + " " );
      }
    }
    function getSolution(userData, pointData){
      var userArr = getSplitArr(userData);
      //console.log(userArr);
     
      var pointArr = getSplitArr(pointData);
      //console.log(pointArr);

      var userPointArr = [];
      for(var i = 0; i < userArr.length; i++){
        userPointArr[i] = [];
        userPointArr[i][0] = userArr[i][0];
        userPointArr[i][1] = userArr[i][1];
        userPointArr[i][2] = 0;
      }
      //console.log(userPointArr);
      for(var i = 0; i < pointArr.length; i++){
        for(var j = 0; j < userPointArr.length; j++){
          if(pointArr[i][1] == userPointArr[j][0]){
            userPointArr[j][2] += Number(pointArr[i][0]); 
            break;           
          }
        }
      }    
      printTable(userPointArr);
      var maxUser = getMaxUser(userPointArr);
      return maxUser;
    }
    var userData = "1001/김철수,";
        userData += "1002/이만수,";
        userData += "1003/이영희";

    var pointData = "1/1001,";
        pointData += "1/1002,";
        pointData += "2/1003,";
        pointData += "1/1001,";
        pointData += "2/1002";
    
    var maxUser = getSolution(userData, pointData);
    console.log(maxUser);
  
  </script>