# SN_CE_EXTRACT_ST

> This table is used to store activity data extracted from the clinical event tables. It is used in Surgery Mgmt Reporting OMF views

**Description:** SurgiNet Clinical Event Extract Summary Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_ID` | DOUBLE | NOT NULL |  | The event_id from the clinical_event table associated with this entry in PDM |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The parent entity id for this clinical event entry |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The parent entity name for this clinical event entry |
| 4 | `PERIOP_DOC_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the perioperative document table, indicating the document assoc. with this clinical event entry |
| 5 | `RESULT_CD` | DOUBLE |  |  | The coded result associated with this clinical event (used when an input field is validated from a codeset) |
| 6 | `RESULT_DT_TM` | DATETIME |  |  | The result associated with this clinical event -- used when the result type is Date/Time |
| 7 | `RESULT_FREE_TEXT` | VARCHAR(255) |  |  | The result associated with this clinical event -- used when the result type is free text |
| 8 | `RESULT_ID` | DOUBLE |  |  | The result associated with this clinical event -- used when the result type is Nomenclature, Item, Provider, or Prsnl Group |
| 9 | `RESULT_PARENT_TABLE` | VARCHAR(50) |  |  | The result parent table associated with this clinical event |
| 10 | `RESULT_TYPE_MEANING` | CHAR(12) |  |  | The CDF meaning for the result type associated with this clinical event |
| 11 | `SN_CE_EXTRACT_ST_ID` | DOUBLE | NOT NULL |  | A unique identifier (primary key) associated with this clinical event |
| 12 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The task assay associated with this clinical event |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERIOP_DOC_ID` | [PERIOPERATIVE_DOCUMENT](PERIOPERATIVE_DOCUMENT.md) | `PERIOP_DOC_ID` |

