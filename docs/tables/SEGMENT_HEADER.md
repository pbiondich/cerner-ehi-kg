# SEGMENT_HEADER

> Contains attributes of the segments within a perioperative document, i.e. Accessed, Discontinued, Not Applicable, etc.

**Description:** Segment Header  
**Table type:** ACTIVITY  
**Primary key:** `SEGMENT_HEADER_ID`  
**Columns:** 22  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_FLAG` | DOUBLE |  |  | An indicator of whether this segment has been accessed for this perioperative document |
| 2 | `ADDL_INFO_IND` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 3 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 5 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 6 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 7 | `DISCONTINUE_REASON_CD` | DOUBLE | NOT NULL |  | The reason this segment was discontinued, i.e. equipment failure, no specimen collected, etc. |
| 8 | `INPUT_FORM_CD` | DOUBLE | NOT NULL |  | The input form associated with this segment being documented. This column will only be populated for segments that use the Form Builder. |
| 9 | `INPUT_FORM_VER_NBR` | DOUBLE |  |  | The version number associated with the input form being documented for this segment. This column will only be populated for segments that use the form builder. |
| 10 | `LAST_CORR_DT_TM` | DATETIME |  |  | The date and time of the last correction to this segment |
| 11 | `LAST_CORR_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 12 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE ***Column |
| 13 | `NOT_APPLICABLE_IND` | DOUBLE |  |  | An indicator of whether or not this segment has been designated as Not Applicable for this perioperative document |
| 14 | `PERIOP_DOC_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the perioperative_document table indicating the perioperative document associated with this segment. |
| 15 | `SEGMENT_HEADER_ID` | DOUBLE | NOT NULL | PK | The primary key, uniquely identifying a row on this table |
| 16 | `SEG_CD` | DOUBLE | NOT NULL |  | The segment being documented for this perioperative document |
| 17 | `SEG_TYPE_FLAG` | DOUBLE |  |  | *** OBSOLETE ***Column |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERIOP_DOC_ID` | [PERIOPERATIVE_DOCUMENT](PERIOPERATIVE_DOCUMENT.md) | `PERIOP_DOC_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [CASE_ATTENDANCE](CASE_ATTENDANCE.md) | `SEGMENT_HEADER_ID` |
| [CASE_TIMES](CASE_TIMES.md) | `SEGMENT_HEADER_ID` |
| [SN_ACUITY_LEVEL](SN_ACUITY_LEVEL.md) | `SEGMENT_HEADER_ID` |
| [SN_IMPLANT_LOG_ST](SN_IMPLANT_LOG_ST.md) | `SEGMENT_HEADER_ID` |
| [SURGICAL_DELAY](SURGICAL_DELAY.md) | `SEGMENT_HEADER_ID` |
| [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SEGMENT_HEADER_ID` |

