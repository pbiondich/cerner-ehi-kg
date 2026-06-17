# ONC_TC_CAL_ITEMS

> Stores the Note text and Prescription order information.

**Description:** ONCOLOGY - TREATMENT CALENDER ITEMS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CAL_ITEM_TYPE_FLAG` | DOUBLE | NOT NULL |  | This tells the type of note stored in ONC_TC_CAL_ITEMS table.(0 - Notes, 1- Prescriptions) |
| 2 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Primary key from LONG_TEXT table. |
| 3 | `OCCURRENCE_DATE_TXT` | VARCHAR(1000) |  |  | To store the occurrence dates of the prescription order. |
| 4 | `ONC_TC_CAL_ITEMS_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Unique foreign key for Orders Table, in this case used for prescriptions. |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It stores the person to whom the prescriptions/ notes are added. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `UPDT_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

