from pathlib import Path
from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, PhotoSize
from model import model_
from handlers import keyboards as kb
from model import get_results_model
from utils.utils import temp_dir


router = Router()


@router.message(Command("start"))
async def help_command(message: Message):
    d = 'Привет! Этот тг-бот - прототип для проекта команды "супчик"\nЗагрузите снимок МРТ и получите результат анализа'
    await message.reply(d, reply_markup=kb.empty)
    f = 'Тестовые снимки тут: https://drive.google.com/drive/folders/155l0AP-Uj0UeAIheJVr8hsRqmlT2vSbp'
    await message.reply(f, reply_markup=kb.empty)


@router.message(F.photo[-1].as_('photo'))
async def process_photo(message: Message, bot: Bot, photo: PhotoSize):
    photo_path = Path(temp_dir, f"{photo.file_id}.jpg")
    a = {
        'glioma': "выявил глиому головного мозга, опухоль первичного характера, которая развивается из глиальных клеток нервной системы.",
        'meningioma': "выявил менингиому, доброкачественную опухоль из клеток оболочек головного мозга.",
        'notumor': "не выявил опухоли.",
        'pituitary': "выявил аденому гипофиза, опухоль железистой ткани передней доли гипофиза."
    }
    await bot.download(photo, photo_path)
    img, verdict, probability = get_results_model(photo_path, model_)
    #image = tf.image.encode_png(img)
    v = f"Наш бот {a[verdict]}"
    await message.reply(v, reply_markup=kb.empty)
    #await message.answer_photo(FSInputFile(path=img))
    #await message.answer_photo(image)
    '''await message.reply(
        f"<b>{result}</b>\n"
    )'''


