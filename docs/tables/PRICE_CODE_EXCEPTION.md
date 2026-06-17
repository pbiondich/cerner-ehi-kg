# PRICE_CODE_EXCEPTION

> Price Code Exception - Stores Price schedule exceptions for default price code.

**Description:** PRICE CODE EXCEPTION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COPAY_PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Indicates default Price schedule for copay. Key of Price Schedule table. |
| 2 | `EXCEPTION_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates type of exception (such as Generic, Brand, Ther. Class, Drug Id) |
| 3 | `FLEXED_TO_PRICE_CODE_CD` | DOUBLE | NOT NULL |  | Allows flexing the price code. Currently it can be flexed by location. |
| 4 | `PARENT_ENTITY` | VARCHAR(32) |  |  | Data source for each exception type. Related to column parent_entity_id. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Value of key field for the table named in column parent_entity. |
| 6 | `PRICE_CODE_CD` | DOUBLE | NOT NULL |  | This is the price code that is being flexed. A price code is a pointer to a group of price schedules, which are the formula used to calculate the price charged for a product when it is ordered. |
| 7 | `PRICE_CODE_EXCEPTION_ID` | DOUBLE | NOT NULL |  | Unique, generated key for the PRICE_CODE_EXCEPTION table. |
| 8 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Indicates Price schedule for exception type. Key of Price Schedule table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VALUE` | VARCHAR(200) |  |  | Used when parent_entity is a free text value (not from a table). Currently, only exception type of "DRUGID" uses this field and will contain the NDC identifier of the Drug. |
| 15 | `VALUE_KEY` | VARCHAR(200) |  |  | Same as Value without special characters and is converted to upper case. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COPAY_PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |

