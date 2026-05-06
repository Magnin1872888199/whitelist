const express = require("express");
const axios = require("axios");

const app = express();

const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
const USERNAME = "Magnin1872888199";
const REPO = "whitelist";

const FILE_PATH = "whitelist.json";

async function getWhitelist() {
  const url = `https://api.github.com/repos/${USERNAME}/${REPO}/contents/${FILE_PATH}`;

  const response = await axios.get(url, {
    headers: {
      Authorization: `token ${GITHUB_TOKEN}`
    }
  });

  const content = Buffer.from(response.data.content, "base64").toString();

  return {
    data: JSON.parse(content),
    sha: response.data.sha
  };
}

async function updateWhitelist(newData, sha) {
  const url = `https://api.github.com/repos/${USERNAME}/${REPO}/contents/${FILE_PATH}`;

  await axios.put(
    url,
    {
      message: "update whitelist",
      content: Buffer.from(
        JSON.stringify(newData, null, 2)
      ).toString("base64"),
      sha: sha
    },
    {
      headers: {
        Authorization: `token ${GITHUB_TOKEN}`
      }
    }
  );
}

app.get("/add", async (req, res) => {
  const nick = req.query.nick;

  const whitelist = await getWhitelist();

  if (!whitelist.data.users.includes(nick)) {
    whitelist.data.users.push(nick);

    await updateWhitelist(whitelist.data, whitelist.sha);

    return res.send("Nick adicionado");
  }

  res.send("Nick já existe");
});

app.get("/remove", async (req, res) => {
  const nick = req.query.nick;

  const whitelist = await getWhitelist();

  whitelist.data.users =
    whitelist.data.users.filter(u => u !== nick);

  await updateWhitelist(whitelist.data, whitelist.sha);

  res.send("Nick removido");
});

app.get("/check", async (req, res) => {
  const nick = req.query.nick;

  const whitelist = await getWhitelist();

  if (whitelist.data.users.includes(nick)) {
    return res.send("Está na whitelist");
  }

  res.send("Não está na whitelist");
});

app.listen(3000, () => {
  console.log("API ONLINE");
});
