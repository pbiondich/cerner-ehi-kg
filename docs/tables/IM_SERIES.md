# IM_SERIES

> IM Series

**Description:** This table contains series information for an imaging study.  
**Table type:** ACTIVITY  
**Primary key:** `IM_SERIES_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IM_MPPS_ID` | DOUBLE | NOT NULL | FK→ | This column contains a foreign key to the IM_MPPS table. |
| 2 | `IM_SERIES_ID` | DOUBLE | NOT NULL | PK | This column contains a meaningless number that only serves to uniquely identify a row. |
| 3 | `MODALITY` | VARCHAR(16) |  |  | This column contains the modality as it was passed from the archive. |
| 4 | `NBR_OF_IMAGES` | DOUBLE |  |  | This column indicates the number of images that are a part of the series. |
| 5 | `OPERATOR_NAME` | VARCHAR(64) |  |  | Name of the operator who performed this series |
| 6 | `OPERATOR_PRSNL_ID` | DOUBLE | NOT NULL |  | Prsnl id (de-aliased version of operator name) |
| 7 | `PERFORMING_PHYSICIAN_NAME` | VARCHAR(64) |  |  | Name of the physician administering this series |
| 8 | `PERFORMING_PHYSICIAN_PRSNL_ID` | DOUBLE | NOT NULL |  | Prsnl ID (de-aliased version of performing physician name) |
| 9 | `PROTOCOL_NAME` | VARCHAR(64) |  |  | This column is only used for MPPS. It contains the protocol used. |
| 10 | `RETRIEVE_AE_TITLE` | VARCHAR(16) |  |  | This column is only used by MPPS |
| 11 | `SERIES_NBR` | DOUBLE |  |  | This column indicates the order of the series within the study. |
| 12 | `SERIES_UID` | VARCHAR(64) | NOT NULL |  | This column contains the Series UID that was assigned by the modality. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IM_MPPS_ID` | [IM_MPPS](IM_MPPS.md) | `IM_MPPS_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [IM_MATCH_EVENT](IM_MATCH_EVENT.md) | `IM_SERIES_ID` |
| [IM_U_NOTIFY](IM_U_NOTIFY.md) | `IM_SERIES_ID` |

