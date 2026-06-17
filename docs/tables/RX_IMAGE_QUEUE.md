# RX_IMAGE_QUEUE

> The queue within PharmNet Order Imaging where orders will be faxed or scanned so that pharmacy users can begin processing.

**Description:** Image Queue  
**Table type:** REFERENCE  
**Primary key:** `IMAGE_QUEUE_ID`  
**Columns:** 9  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IMAGE_QUEUE_CD` | DOUBLE | NOT NULL |  | The code value of the Image Queue. |
| 2 | `IMAGE_QUEUE_ID` | DOUBLE | NOT NULL | PK | The generated, primary key for RX_IMAGE_QUEUE. |
| 3 | `NCLUD_CMPLTD_IMAGE_FLAG` | DOUBLE | NOT NULL |  | Flag to indicate to include completed images in a queue. |
| 4 | `NCLUD_DEL_IMAGE_FLAG` | DOUBLE | NOT NULL |  | Flag to indicate to include deleted images in a given queue. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [RX_IMAGE_QUEUE_LOC_RELTN](RX_IMAGE_QUEUE_LOC_RELTN.md) | `IMAGE_QUEUE_ID` |
| [RX_IMAGE_QUEUE_PRSNL_RELTN](RX_IMAGE_QUEUE_PRSNL_RELTN.md) | `IMAGE_QUEUE_ID` |
| [RX_IMG_IMGQUE_RELTN](RX_IMG_IMGQUE_RELTN.md) | `IMAGE_QUEUE_ID` |
| [RX_IMG_IMGQUE_RELTN_HX](RX_IMG_IMGQUE_RELTN_HX.md) | `IMAGE_QUEUE_ID` |

