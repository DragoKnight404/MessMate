import { useState } from "react";
import starIcon from "../assets/Star.png";
import { AiFillStar } from "react-icons/ai";

const foodItems = [
  {
    img: "https://cdn.usegalileo.ai/stability/b5ff7d3a-b8a5-4dd3-9809-85efaac70cdd.png",
    name: "Avocado Toast",
    price: "$12.99",
    tags: "Breakfast, Vegan",
    rating: 3.9,
    quantity: 5,
    ingredients: ["Avocado", "Bread", "Olive Oil", "Salt"],
  },
  {
    img: "https://cdn.usegalileo.ai/stability/934464b5-541f-4462-a71f-16d31f5ed574.png",
    name: "Acai Bowl",
    price: "$9.99",
    tags: "Breakfast",
    rating: 4.5,
    quantity: 9,
    ingredients: ["Acai", "Banana", "Granola", "Honey"],
  },
  {
    img: "https://cdn.usegalileo.ai/sdxl10/b0457ffa-d652-4e91-83ac-4f1a77121a9c.png",
    name: "Egg and Cheese Biscuit",
    price: "$7.99",
    tags: "Breakfast",
    rating: 4.1,
    quantity: 1,
    ingredients: ["Egg", "Cheese", "Biscuit", "Butter"],
  },
  {
    img: "https://cdn.usegalileo.ai/sdxl10/0ab7814c-86c4-4d9e-a6f3-1ab672998a06.png",
    name: "Green Smoothie",
    price: "$5.99",
    tags: "Drink",
    rating: 4.9,
    quantity: 3,
    ingredients: ["Spinach", "Banana", "Almond Milk", "Chia Seeds"],
  },
  {
    img: "https://cdn.usegalileo.ai/stability/b5ff7d3a-b8a5-4dd3-9809-85efaac70cdd.png",
    name: "Avocado Toast",
    price: "$12.99",
    tags: "Breakfast, Vegan",
    quantity: 4,
    rating: 3.9,
    ingredients: ["Avocado", "Bread", "Olive Oil", "Salt"],
  },
];

const OrderDetails = ({closeModal}) => {



    const [rating,setRating] = useState(0);
    const [hover,setHover] = useState(0);
    const [reviewText,setReviewText] = useState("");

    const handleSubmitReview = async (e) => {
        e.preventDefault();
    }

  return (
    <div className=" backdrop-blur-lg ">
      <div className=" w-max h-[80vh] flex flex-col items-start justify-start border-none bg-white   p-5  rounded-md overflow-y-scroll scrollable-grid ">
        <div className=" w-full flex flex-row items-start justify-between mb-5 ">
          <h1 className="text-3xl font-bold">Order Details</h1>
          <button className=" z-20 " onClick={closeModal}>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>

        <div className="flex flex-col items-start justify-start w-full ">
          {foodItems.map((item, index) => (
            <div key={index} className="flex flex-row gap-3 pb-3 w-full ">
              <div
                className="w-full flex items-end justify-end bg-center bg-no-repeat aspect-square bg-cover rounded-xl min-w-[100px] max-w-[120px]"
                style={{ backgroundImage: `url(${item.img})` }}
              >
  
              </div>
              <div className="flex flex-col justify-between h-full text-colorText">
                <div>
                  <p className="text-blackText text-base font-medium leading-normal">
                    {item.name}
                  </p>
                  <p className="text-reddish text-sm font-bold leading-normal">
                    {item.quantity} * {item.price}
                  </p>
                  <p className="text-colorText text-sm font-normal leading-normal">
                    Ingredients: {item.ingredients.join(", ")}
                  </p>
                  <p className="text-blackText text-sm font-normal leading-normal">
                    {item.tags}
                  </p>
                  <div className="flex items-center gap-[6px]">
                    <span className="flex items-center gap-[6px] text-colorText text-sm font-bold leading-normal">
                      <img src={starIcon} className="w-[15px]" alt="" /> {item.rating}
                    </span>
                    <span className="text-colorText text-sm font-normal leading-normal">
                      (272)
                    </span>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        {/* <div className=" border-t-4 w-full border-blackText mt-5 rounded-md" >
        </div> */}
        <p className="text-blackText text-base font-bold leading-tight mt-5 ">
              Total : $71.94
        </p>

        <form className="w-full mt-3">
      <div>
        <h3 className="  text-headingColor text-[16px] leading-6 font-semibold mb-4 mt-0 ">
          How would you rate the overall experience?*
        </h3>

        <div>
          {[...Array(5).keys()].map((_,index) => {
            index += 1;
            return (
              <button
                key={index}
                type="button"
                className={`${
                  index <= ((rating && hover) || hover)
                  ? "text-[#FEB60D]"
                  : "text-gray-200"
                } bg-transparent border-none outline-none text-[22px] cursor-pointer `}
                onClick={() => setRating(index)}
                onMouseEnter={() => setHover(index)}
                onMouseLeave={() => setHover(rating)}
                onDoubleClick={() => {
                  setHover(0);
                  setRating(0);
                }}
              >
                <span>
                  <AiFillStar />  
                </span>
              </button>
            );
          })}
        </div>
      </div>
          
      <div className="mt-3">
      <h3 className="  text-headingColor text-[16px] leading-6 font-semibold mb-4 mt-0 ">
          Share your feedback or suggestions*
        </h3>

        <textarea className=" border border-solid border-[#0066ff34] focus:outline outline-primaryColor w-full px-4 py-3 rounded-md " rows="5"
        placeholder="Write your message"
        onChange={e => setReviewText(e.target.value)}
        ></textarea>
      </div>

      <button onClick={handleSubmitReview} className="btnColored mt-3">
        Submit Feedback 
      </button>

    </form>


        
      </div>
    </div>
  );
};



export default OrderDetails;
