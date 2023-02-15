<script>
    /*
        \n 은 줄바꿈이다.  구분자도 (\n 으로 넣으면 잘잘린다.)

         문제1) 위 데이터 는  각각의 회원이 물건을 구입가격들 을 기록한 내용이다.
		 		회원별 구입 총합을 테이블로 만들려고한다.
			    데이터는 아래와 같이 나올수있도록 result 에 저장후 출력 
				
				10001 김철수 2670
				10002 이영희 1950 
				10003 유재석 4080
				10004 박명수 7130
    */
	function getCheckUser(userTable , userNumber){
		for(var i = 0; i < userTable.length; i++){
			if(userTable[i][0] == userNumber){
				return true;
			}
		}
		return false;
	}
	function getTotalArr(splitArr){
		var userTable = [];
		userTable[0] = [];
		var arr = [splitArr[0][0], splitArr[0][1], 0];
		userTable[0] = arr;
		for(var i = 1; i < splitArr.length; i++){
			if(getCheckUser(userTable , splitArr[i][0]) == false){
				var temp = [splitArr[i][0], splitArr[i][1], 0];
				userTable.push(temp);
			}
		}
		//console.log(userTable);
		for(var i = 0; i < splitArr.length; i++){
			for(var j = 0; j < userTable.length; j++){
				if(splitArr[i][0] == userTable[j][0]){
					userTable[j][2] += Number(splitArr[i][2]);
				}
			}
		}
		return userTable;

	}
	function getSplitArr(data){
		var arr = [];
		var dataStr = data.split("\n");
		for(var i = 0; i < dataStr.length; i++){
			var temp = dataStr[i].split("/");
			arr[i] = [];
			arr[i][0] = temp[0];
			arr[i][1] = temp[1];
			arr[i][2] = Number(temp[2]);
		}
		return arr;
	}
	function getSolution(data){
		var splitArr  = getSplitArr(data);
		//console.log(splitArr);
		var totalArr = getTotalArr(splitArr);
		//console.log(totalArr);
		return totalArr;
	}

    var data ="";
		data += "10001/김철수/600\n";
		data += "10002/이영희/800\n";
		data += "10001/김철수/1400\n";
		data += "10003/유재석/780\n";
		data += "10002/이영희/950\n";
		data += "10004/박명수/330\n";
		data += "10001/김철수/670\n";
		data += "10003/유재석/3300\n";
		data += "10002/이영희/200\n";
		data += "10004/박명수/6800\n";
		data = data.substring(0 , data.length-1); // 마지막 글삭제 
		console.log(data);
    	var result = getSolution(data);
		console.log(result);
  </script>