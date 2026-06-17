# RX_IMAGE_HX

> Stores the status hostiry of the order as well as who changed the status and when.

**Description:** Pharmacy Order Image History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | The date time that an action was taken on an image. |
| 2 | `ACTION_TZ` | DOUBLE | NOT NULL |  | The time zone associated with ACTION_DT_TM. |
| 3 | `IMAGE_HX_ID` | DOUBLE | NOT NULL |  | Unique, generated identifier for RX_IMAGE_HX. |
| 4 | `IMAGE_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for images within the Pharmacy Order Imaging data model. |
| 5 | `STATUS_CD` | DOUBLE | NOT NULL |  | The current status of the image. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IMAGE_ID` | [RX_IMAGE](RX_IMAGE.md) | `IMAGE_ID` |

