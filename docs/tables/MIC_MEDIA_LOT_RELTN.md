# MIC_MEDIA_LOT_RELTN

> This table stores the relationship between a media observation and the associated media lot(s) used for the observation.

**Description:** Microbiology Media Lot Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOT_INFORMATION_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique identifier of the related PCS_LOT_INFORMATION row. |
| 2 | `MEDIA_CD` | DOUBLE | NOT NULL |  | This field contains the code value of the specific type of media identified for this procedure. Media types are defined on code set 2051 Specimen Containers. |
| 3 | `MEDIA_LOT_RELTN_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the media/lot relationship. |
| 4 | `MEDIA_SEQ` | DOUBLE | NOT NULL | FK→ | This field contains the media_seq associated with the related MIC_ORGANISM_OBSERVATION row. |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique value assigned to each orderable procedure associated with an order. For example: if there are two procedures on the same accession number, then each procedure will have a unique order id. |
| 6 | `RESULT_SCHEDULE_ID` | DOUBLE | NOT NULL |  | This field contains the unique identifier of the related MIC_QC_RESULT_SCHEDULE row. |
| 7 | `TASK_LOG_ID` | DOUBLE | NOT NULL | FK→ | This field contains the task_log_id associated with the related MIC_ORGANISM_OBSERVATION row. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_INFORMATION_ID` | [PCS_LOT_INFORMATION](PCS_LOT_INFORMATION.md) | `LOT_INFORMATION_ID` |
| `MEDIA_SEQ` | [MIC_ORGANISM_OBSERVATION](MIC_ORGANISM_OBSERVATION.md) | `MEDIA_SEQ` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `TASK_LOG_ID` | [MIC_ORGANISM_OBSERVATION](MIC_ORGANISM_OBSERVATION.md) | `TASK_LOG_ID` |

