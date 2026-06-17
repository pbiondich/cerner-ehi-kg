# SEGMENT_GRP_REFERENCE

> Contains attributes of a segment group, including the document type that the group is associated with

**Description:** Segment Group Reference  
**Table type:** REFERENCE  
**Primary key:** `SEG_GRP_CD`  
**Columns:** 18  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context associated with the creation of this row |
| 6 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was created |
| 7 | `CREATE_PRSNL_ID` | DOUBLE |  |  | The person who created/inserted this row. |
| 8 | `CREATE_TASK` | DOUBLE |  |  | The task associated with the creation of this row |
| 9 | `DOC_TYPE_CD` | DOUBLE |  |  | The document type associated with this segment group, i.e. OR Nursing Record, Preop Nursing Assessment. |
| 10 | `SEG_GRP_CD` | DOUBLE | NOT NULL | PK | The primary key, uniquely identifying a segment group. |
| 11 | `SEG_GRP_SEQ` | DOUBLE |  |  | The sequence of this segment group within a document type. |
| 12 | `SEG_IND` | DOUBLE |  |  | An indicator of whether or not this is a single-segment segment group (1=more than one) |
| 13 | `SURG_AREA_CD` | DOUBLE |  |  | The surgical area associated with this segment group. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SEGMENT_REFERENCE](SEGMENT_REFERENCE.md) | `SEG_GRP_CD` |
| [SEG_GRP_SEQ_R](SEG_GRP_SEQ_R.md) | `SEG_GRP_CD` |

