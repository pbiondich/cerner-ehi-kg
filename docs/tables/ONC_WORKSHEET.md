# ONC_WORKSHEET

> Stores the oncology doc set and anatomy pathology association information

**Description:** ONCOLOGY WORKSHEET ASSOCIATION  
**Table type:** REFERENCE  
**Primary key:** `ONC_WORKSHEET_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CKI_IDENTIFIER` | VARCHAR(50) |  |  | External identifier for this pattern,used with CKI_SOURCE to form a unique external identifier. |
| 4 | `CKI_SOURCE` | VARCHAR(12) |  |  | key value from SCR_PATTERN table, in this case used get cki_source information for the worksheet from SCR_PATTERN. |
| 5 | `DOC_SET_REF_ID` | DOUBLE | NOT NULL | FK→ | Primary key from DOC_SET_REF table,in this case used get the doc set information from DOC_SET_REF . |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `ENTRY_MODE_CD` | DOUBLE | NOT NULL |  | Indicates the UI mechanism to be used for data entry against this template. |
| 8 | `ONC_WORKSHEET_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 9 | `SCR_PATTERN_ID` | DOUBLE | NOT NULL | FK→ | Primary key from SCR_PATTERN table, in this case used get wokrsheet information from SCR_PATTERN. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_SET_REF_ID` | [DOC_SET_REF](DOC_SET_REF.md) | `DOC_SET_REF_ID` |
| `SCR_PATTERN_ID` | [SCR_PATTERN](SCR_PATTERN.md) | `SCR_PATTERN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ONC_TASK_SENT_RELTN](ONC_TASK_SENT_RELTN.md) | `ONC_WORKSHEET_ID` |

