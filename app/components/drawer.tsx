"use client";

import * as React from "react";

import {
  Drawer,
  Button,
  Typography,
  IconButton,
  List,
  Chip,
  Card,
  Collapse,
  Input,
  Avatar,
} from "@material-tailwind/react";
import { BookMarked, Menu, Search, SquareLibrary, X } from "lucide-react";

const Links = [
  {
    icon: Search,
    title: "주제 검색",
    href: "#",
  },
  {
    icon: SquareLibrary,
    title: "테마 선택",
    href: "#",
  },
  {
    icon: BookMarked,
    title: "즐겨찾기 모음",
    href: "#",
  },
];

export default function DrawerWithNavigation() {
  const [isOpen, setIsOpen] = React.useState(false);

  return (
    <Drawer>
      <Drawer.Trigger as={IconButton} variant="ghost" className="text-white">
        <Menu className="size-10" />
      </Drawer.Trigger>
      <Drawer.Overlay>
        <Drawer.Panel placement="right" className="p-0">
          <div className="flex items-center justify-between gap-4">
            <Drawer.DismissTrigger
              as={IconButton}
              size="sm"
              variant="ghost"
              color="secondary"
              className="absolute right-2 top-2"
              isCircular
            >
              <X />
            </Drawer.DismissTrigger>
          </div>
          <Card className="border-none shadow-none">
            <Card.Header className="m-0 flex h-max items-center gap-2 px-3 pb-3 pt-4">
              <Typography className="font-semibold">메뉴</Typography>
            </Card.Header>
            <Card.Body className="p-3">
              <List className="mt-3">
                {Links.map(({ icon: Icon, title, href }) => (
                  <List.Item key={title}>
                    <List.ItemStart>
                      <Icon className="h-[18px] w-[18px]" />
                    </List.ItemStart>
                    {title}
                  </List.Item>
                ))}
              </List>
            </Card.Body>
            <Card.Footer className="p-3"></Card.Footer>
          </Card>
        </Drawer.Panel>
      </Drawer.Overlay>
    </Drawer>
  );
}
