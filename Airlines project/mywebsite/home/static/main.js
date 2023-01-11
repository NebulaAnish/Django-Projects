const nav = document.querySelector(".nav")
window.addEventListener("scroll",(e)=>{
   if (scrollY >nav.offsetHeight+150){
      nav.classList.add('active')
   }
   else {
      nav.classList.remove("active")
   }
})

console.log("Test")