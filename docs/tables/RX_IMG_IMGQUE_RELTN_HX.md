# RX_IMG_IMGQUE_RELTN_HX

> Stored the historical relationship between an image and a queue.

**Description:** Pharmacy Order Image Image Queue Relation History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPLETED_DT_TM` | DATETIME |  |  | The time the image was either cancelled or completed. |
| 2 | `COMPLETED_TZ` | DOUBLE | NOT NULL |  | Time zone associated with COMPLETED_DT_TM. |
| 3 | `IMAGE_ID` | DOUBLE | NOT NULL | FK→ | The unique, generated identifier for images within the Pharmacy Order Imaging data model. |
| 4 | `IMAGE_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | The generated, primary key for RX_IMAGE_QUEUE. |
| 5 | `IMG_IMGQUE_RELTN_HX_ID` | DOUBLE | NOT NULL |  | Unique, generated identifier for RX_IMG_IMGQUE_RELTN_HX. |
| 6 | `ROUTE_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Indicates if the image was system or manually routed and who routed the image if manual. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IMAGE_ID` | [RX_IMAGE](RX_IMAGE.md) | `IMAGE_ID` |
| `IMAGE_QUEUE_ID` | [RX_IMAGE_QUEUE](RX_IMAGE_QUEUE.md) | `IMAGE_QUEUE_ID` |
| `ROUTE_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

