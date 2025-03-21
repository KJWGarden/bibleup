import { Button, IconButton } from "@material-tailwind/react";
import DrawerWithNavigation from "./components/drawer";
import { Bookmark, Heart, MessageSquareMore } from "lucide-react";

export default function Home() {
  return (
    <div className="h-full w-full">
      <div className="w-screen flex py-5  px-5 justify-end">
        <DrawerWithNavigation />
      </div>
      <section className="w-screen h-screen flex">
        <main className="flex w-[90vw] justify-center items-center text-white text-2xl">
          메인섹션입니다.
        </main>
        <aside className="h-screen flex-col text-white space-y-10 content-center ">
          <div>
            <IconButton variant="ghost" className="text-white">
              <MessageSquareMore className="size-10" />
            </IconButton>
          </div>
          <div>
            <IconButton variant="ghost" className="text-white ">
              <Heart className="size-10" />
            </IconButton>
          </div>
          <div>
            <IconButton variant="ghost" className="text-white">
              <Bookmark className="size-10" />
            </IconButton>
          </div>
        </aside>
      </section>
      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center"></footer>
    </div>
  );
}
