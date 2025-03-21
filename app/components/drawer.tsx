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
import { Menu, X } from "lucide-react";

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
              <Avatar
                size="xs"
                src="https://raw.githubusercontent.com/creativetimofficial/public-assets/master/ct-assets/logo.png"
                alt="brand"
              />
              <Typography className="font-semibold">
                Material Tailwind
              </Typography>
            </Card.Header>
            <Card.Body className="p-3"></Card.Body>
            <Card.Footer className="p-3"></Card.Footer>
          </Card>
        </Drawer.Panel>
      </Drawer.Overlay>
    </Drawer>
  );
}
