import React, { useState, useEffect, useRef } from "react";

const usePreventLeave = () => {
  const listener = event => {
    event.preventDefault();
    event.returnValue = ""; // 이 코드를 넣어줘야 작동한다
  };
  // 사용자의 요청에서 보호하기 위한
  const enablePrevent = () => window.addEventListener("beforeunload", listener);
  const disablePrevent = () =>
    window.removeEventListener("beforeunload", listener);
  return { enablePrevent, disablePrevent };
};

const App = () => {
  const { enablePrevent, disablePrevent } = usePreventLeave();
  return (
    <div className="App">
      <button onClick={enablePrevent}>Protect</button>
      <button onClick={disablePrevent}>Unprotect</button>
    </div>
  );
};

export default App;

// 07
// const useConfirm = (message = "", onConfirm, onCancle) => {
//   // if (typeof callback !== "function") {
//   //   return;
//   // }
//   const confirmAction = () => {
//     if (confirm(message)) {
//       onConfirm();
//     } else {
//       onCancle();
//     }
//   };
//   return confirmAction;
// };

// const App = () => {
//   const deleteWorld = () => console.log("delete the word");
//   const abort = () => console.log("Aborted");
//   const confirmDelete = useConfirm("Are you sure", deleteWorld, abort);
//   return (
//     <div className="App">
//       <button onClick={confirmDelete}>delete</button>
//     </div>
//   );
// };

// // 06
// // useClick 을 사용해서 useRef() 만들었다
// const useClick = onClick => {
//   // if (typeof onClick !== "fuction") {
//   //   return;
//   // }
//   const element = useRef();
//   // 여기서 fucntion 을 만들어준다
//   useEffect(() => {
//     //
//     // element 존재 여부 확인
//     if (element.current) {
//       // 존재하면 addEventListener 실행
//       element.current.addEventListener("click", onClick);
//     }
//     return () => {
//       if (element.current) {
//         element.current.removeEventListener("click", onClick);
//       }
//     };
//   }, []); // dep 가 비어있기 때문에 update 는 신경안써도 갠춘
//   return element;
// };

// const App = () => {
//   const sayHello = () => console.log("say hello ");
//   const title = useClick(sayHello);
//   return (
//     <div className="App">
//       <h1 ref={title}>HI</h1>
//     </div>
//   );
// };

// // 05;
// const useTitle = initialTitle => {
//   const [title, setTitle] = useState(initialTitle);
//   const updateTitle = () => {
//     const htmlTitle = document.querySelector("title");
//     htmlTitle.innerText = title;
//   };
//   useEffect(updateTitle, [title]); // dependency 는 매우 유용하다!

//   return setTitle; // title 을 업데이트 하기 위해
// };

// const App = () => {
//   const titleUpdate = useTitle("Loading...");
//   // 시간지연 설정
//   setTimeout(() => titleUpdate("Home"), 5000);  // 5초 후에 Hoem으로 변경

//   return (
//     <div className="App">
//       <div>HI</div>
//     </div>
//   );
// };

// // 04. useEffect
// const App = () => {
//   // useEffect 는 componentDidMount의 역할을 해서 새로 고침을 하면 sayHello 를 실행한다.
//   // 2개의 인자를 받는데도
//   // 첫번째는 function 으로 effect - 두번째 인자를 설정하지 않는다면 계속 sayHello 작동
//   // 두번째는 deps - 리스트에 있는 값일 때만 값이 변하도록 활성화
//   const sayHello = () => console.log("Hello");

//   const [number, setNumber] = useState(0);
//   const [aNumber, setAnumber] = useState(0);
//   // number가 변할때만 sayHello 가 작동, aNumber 때는 작동 ㄴㄴ
//   useEffect(sayHello, [number]);

//   // useEffect(sayHello, []);  // 빈리스트면 어떠한 경우에도 sayHello 가 작동하지 않는다.
//   return (
//     <div className="App">
//       <div>HI</div>
//       <button onClick={() => setNumber(number + 1)}>{number}</button>
//       <button onClick={() => setAnumber(aNumber + 1)}>{aNumber}</button>
//     </div>
//   );
// };

// // 03. useTabs
// const content = [
//   {
//     tab: "Section 1",
//     content: "I'm the content of the Section 1"
//   },
//   {
//     tab: "Section 2",
//     content: "I'm the content of the Section 2"
//   }
// ];

// const useTabs = (initialTab, allTabs) => {

//   // if (!allTabs || Array.isArray(allTabs)) {
//   //   return; // 배열이 아닐때 return 한다
//   // }

//   // 6. useState 를 바꾼다.
//   const [currentIndex, setCurrentIndex] = useState(initialTab); // useSate 가 항상 intialTab 을 갖는다. )
//   return {
//     // 7. 그래서 currentItem 의 currentIndex 를 바꿔줄거고
//     // 8. 그래서 모든것을 새로고침 하는 것입니다아....
//     currentItem: allTabs[currentIndex],
//     // 5. setCurrentIndex 의 item 을 바꾸고 그것은
//     changeItem: setCurrentIndex
//   };
// };

// const App = () => {
//   const { currentItem, changeItem } = useTabs(0, content);
//   return (
//     <div className="App">
//       {/* 1. index 는 0 또는 1 이어야 하고  */}
//       {content.map((section, index) => (
//         // 2. 모든 버튼은 onClick(이벤트) 를 가진다.
//         // 3. 인덱스와 상관없이 changeItem(index) 를 실행하고
//         // 4. index 는 index 안에 있는 값인 0 또는 1로 바꿔준다.

//         <button onClick={() => changeItem(index)}>{section.tab}</button>
//       ))}
//       <div>{currentItem.content}</div>
//     </div>
//   );
// };

// // 02. userInput
// const useInput = (initialValue, validator) => {
//   // 1. 매번 validator 은 바뀐다.
//   const [value, setValue] = useState(initialValue);
//   // 변화를 주기 전에 기본값(soo) 을 value 와 함께 return 하기
//   const onChange = event => {
//     const {
//       target: { value }
//     } = event;
//     // 유효성 검증 추가
//     let willUpdate = true;
//     // 2. validator 가 function 이면
//     if (typeof validator === "function") {
//       willUpdate = validator(value);
//     }
//     // 3, willUpdate 에 validator 의 결과가 업로드 된다.
//     if (willUpdate) {
//       setValue(value); // 6. true 이면 업데이트 될것이다.
//     } else {
//       alert("@ 는 입력 ㄴㄴ");
//     }
//   };
//   return { value, onChange };
// };

// const App = () => {
//   // 4. 그리고 그 validator 은 아래와 같다.
//   const maxLen = value => !value.includes("@"); // 5. 결과는 t/f 일것이고

//   const name = useInput("soo", maxLen);
//   return (
//     <div className="App">
//       <h1>HI</h1>
//       {/* <input placeholder="Name" value={name.value} onChange={name.onChange} /> */}
//       <input placeholder="Name" {...name} />{" "}
//       {/* 둘다 똑같은 기능을 한다. name 안에 있는 것을 풀어준다.  */}
//     </div>
//   );
// };

// // 01. hooks
// // Arrow fuction 사용하는 것은 자기 마음~
// // 훠어어얼씬 짧고 깔끔하다!!
// const App = () => {
//   const [item, setItem] = useState(1);
//   // 1 이 최초의 value 이고, setItem 은 value 값을 변경해준다.

//   const incrementItem = () => setItem(item + 1);
//   const decrementItem = () => setItem(item - 1);
//   return (
//     <div className="App">
//       <h1>Hello {item} </h1>

//       <button onClick={incrementItem}>+</button>
//       <button onClick={decrementItem}>-</button>
//     </div>
//   );
// };
