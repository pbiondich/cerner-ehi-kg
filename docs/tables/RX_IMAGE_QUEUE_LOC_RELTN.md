# RX_IMAGE_QUEUE_LOC_RELTN

> Stores the relationship between an RX_IMAGE_QUEUE and a LOCATION.

**Description:** Image Queue Location Relation  
**Table type:** REFERENCE  
**Primary key:** `IMAGE_QUEUE_LOC_RELTN_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IMAGE_QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Queue that is involved in this Queue/Location relationship. |
| 2 | `IMAGE_QUEUE_LOC_RELTN_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the Image Queue to Location relationship. |
| 3 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Identifies the specific LOCATION that is involved in this Image Queue to Location relationship. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IMAGE_QUEUE_ID` | [RX_IMAGE_QUEUE](RX_IMAGE_QUEUE.md) | `IMAGE_QUEUE_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_IMAGE_QUEUE_TIME](RX_IMAGE_QUEUE_TIME.md) | `IMAGE_QUEUE_LOC_RELTN_ID` |

