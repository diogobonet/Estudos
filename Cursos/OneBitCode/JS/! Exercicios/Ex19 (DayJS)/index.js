let dayjs = require("dayjs")
let customParseFormat = require('dayjs/plugin/customParseFormat')
let relativeTime = require('dayjs/plugin/relativeTime')
dayjs.extend(customParseFormat, relativeTime)

function birthdayDate(date) {
    let birthdayDate = dayjs(date)
    let actualDate = dayjs(new Date()).format('DD/MM/YYYY')
    let actualYear = dayjs(new Date()).$y
    let yearDifference = dayjs(date).diff(actualDate, 'years')
    let nextDate = dayjs().diff(date, 'days')


    console.log(`Dia atual (hoje): ${actualDate}`)
    console.log(`A sua idade é ${Math.abs(yearDifference)} anos.`)
    console.log(`Sua próxima data de aniversário é ${nextDate}`)
    console.log(`Faltam ${nextDate} dias para seu próximo aniversário`)
    console.log()
}

birthdayDate("03/09/2004")