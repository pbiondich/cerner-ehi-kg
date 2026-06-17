# RAD_FILM_ADJUST

> The Rad_Film_Adjust table contains repeat and waste information about a particular order.

**Description:** Rad Film Adjustments  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLETE_DT_TM` | DATETIME |  |  | The Complete_Dt_Tm captures the date and time that the exam was performed. |
| 2 | `COMPLETE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 3 | `FILM_SIZE_CD` | DOUBLE | NOT NULL |  | The Film_Size_Cd identifies a specific size of film that was used while performing the exam. |
| 4 | `FILM_TYPE_CD` | DOUBLE | NOT NULL |  | The Film_Type_Cd identifies a specific type of film that was used while performing the exam. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The Order_Id is a foreign key to the Order_Radiology table. It identifies the order which the film adjustments are being recorded for. |
| 6 | `REPEAT_WASTE_CD` | DOUBLE | NOT NULL |  | The Repeat_Waste_Cd identifies if the if the film was repeated or wasted. |
| 7 | `RESPONSIBLE_ID` | DOUBLE | NOT NULL | FK→ | The Responsible_Id identifies the person responsible for the use of additional film. |
| 8 | `SEQUENCE` | DOUBLE | NOT NULL |  | The Sequence is used along with the Order_Id to uniquely identify a row in the Rad_Film_Adjust table. It serves no other purpose other than to uniquely identify the row. |
| 9 | `STD_QUANTITY` | DOUBLE |  |  | The Std_Quantity stores the number of films that should be used while performing the exam. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `WASTE_QUANTITY` | DOUBLE |  |  | The Waste_Quantity stores the number of films that were wasted while performing the exam. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `RESPONSIBLE_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

