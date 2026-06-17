# WF_STFG_HDR

> This table stores the header information of the predictive calculation model in Workforce solution.

**Description:** Workforce staffing header  
**Table type:** ACTIVITY  
**Primary key:** `WF_STFG_HDR_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CENSUS` | DOUBLE |  |  | Census at the time the staffing recommendation was generated. |
| 2 | `COMMENT_TEXT` | VARCHAR(300) |  |  | Text comments when manually submitting staffing requirements. |
| 3 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location of the staffing recommendation |
| 4 | `MANUAL_IND` | DOUBLE | NOT NULL |  | Indicates if the shift has been submitted manually or automatically by the system. |
| 5 | `PENDING_ADMITS` | DOUBLE |  |  | Pending admits coming into the location |
| 6 | `PENDING_DISCHARGES` | DOUBLE |  |  | Pending discharges leaving the location |
| 7 | `QUEUE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the record in the CQM_FSIESO_QUE table that is related to this staffing header record. |
| 8 | `QUEUE_SUBMIT_DT_TM` | DATETIME |  |  | The date and time the staffing recommended was sent to the ESO (External System Outbound) server. |
| 9 | `REASON_CD` | DOUBLE | NOT NULL |  | Reason the staffing recommendation was manually updated. |
| 10 | `SHIFT_DT_TM` | DATETIME |  |  | Date of the shift being recommended |
| 11 | `SUBMITTED_DT_TM` | DATETIME |  |  | Date and time the shift was submitted |
| 12 | `SUBMITTED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel who submitted the shift |
| 13 | `TL_TIME_FRAME_ID` | DOUBLE | NOT NULL | FK→ | The associated task list time frame |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `USER_ADMITS` | DOUBLE |  |  | Manually (user) entered pending admits |
| 20 | `USER_DISCHARGES` | DOUBLE |  |  | Manually (user) entered pending discharges |
| 21 | `WF_STFG_HDR_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a workforce header of staffing requests. |
| 22 | `WF_STFG_REQ_ID` | DOUBLE | NOT NULL | FK→ | Associates staffing requirements calculator data |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `QUEUE_ID` | [CQM_FSIESO_QUE](CQM_FSIESO_QUE.md) | `QUEUE_ID` |
| `SUBMITTED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TL_TIME_FRAME_ID` | [TL_TIME_FRAME](TL_TIME_FRAME.md) | `TL_TIME_FRAME_ID` |
| `WF_STFG_REQ_ID` | [WF_STFG_REQ](WF_STFG_REQ.md) | `WF_STFG_REQ_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [WF_STFG_LINE](WF_STFG_LINE.md) | `WF_STFG_HDR_ID` |
| [WF_STFG_REQ_HDR_RELTN](WF_STFG_REQ_HDR_RELTN.md) | `WF_STFG_HDR_ID` |

