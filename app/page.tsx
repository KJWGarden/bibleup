"use client";

import DrawerWithNavigation from "./components/drawer";
import { Bookmark, Heart, MessageSquareMore } from "lucide-react";
import CommentDrawer from "./components/commentDrawer";
import IconButton from "@material-tailwind/react/dist/components/icon-button";
import { useState } from "react";

export default function Home() {
  const [isLikeClick, setIsLikeClick] = useState(false);
  const [isMarkClick, setIsMarkClick] = useState(false);

  return (
    <div className="h-full w-full">
      <div className="flex py-4  px-4 justify-end ">
        <div className="bg-black bg-opacity-75 rounded-lg p-1">
          <DrawerWithNavigation />
        </div>
      </div>
      <section className="w-screen h-screen flex">
        <main className="flex w-[90vw] justify-center items-center text-white text-2xl">
          메인섹션입니다.
        </main>
        <aside className="h-screen flex flex-col text-white space-y-10 content-center justify-center px-4">
          <div className="bg-black rounded-lg p-1 bg-opacity-75">
            <CommentDrawer />
          </div>
          <div className="bg-black rounded-lg p-1 bg-opacity-75">
            <IconButton
              variant="ghost"
              className="text-white "
              onClick={() => setIsLikeClick((prev) => !prev)}
            >
              <Heart
                className={`size-10 ${
                  isLikeClick ? "text-red-600" : "text-white"
                }`}
              />
            </IconButton>
          </div>
          <div className="bg-black rounded-lg p-1 bg-opacity-75">
            <IconButton
              variant="ghost"
              className="text-white"
              onClick={() => setIsMarkClick((prev) => !prev)}
            >
              <Bookmark
                className={`size-10 ${
                  isMarkClick ? "text-blue-400" : "text-white"
                }`}
              />
            </IconButton>
          </div>
        </aside>
      </section>

      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center"></footer>
    </div>
  );
}
