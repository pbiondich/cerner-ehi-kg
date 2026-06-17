# NC_CHARTED_SECTION

> Maintains activity of a charting section.

**Description:** Nursing - Charting View  
**Table type:** ACTIVITY  
**Primary key:** `NC_CHARTED_SECTION_ID`  
**Columns:** 22  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CHARTED_SECTION_CLOB` | LONGTEXT |  |  | A JSON formatted string containing the representation of the charted section activity. |
| 6 | `CLINICAL_DT_TM` | DATETIME |  |  | The clinically relevent date of the charted section. |
| 7 | `CLOB_TYPE_FLAG` | DOUBLE | NOT NULL |  | Represents the type of data stored in the JSON clob. |
| 8 | `CLOUD_CHARTING_SECTION_IDENT` | VARCHAR(255) | NOT NULL |  | Represents the cloud reference identifier for the charting section. |
| 9 | `CREATE_DT_TM` | DATETIME |  |  | Thd date and time this row was created. |
| 10 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel ID of the person who created the row in the table |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The patient's encounter associated to the section. |
| 12 | `LAST_UPDT_DT_TM` | DATETIME |  |  | Last date and time this row was updated. |
| 13 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that last updated the data on this row. |
| 14 | `NC_CHARTED_SECTION_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the NC_CHARTED_SECTION table. |
| 15 | `NC_CHARTED_VIEW_ID` | DOUBLE |  | FK→ | The Charted View that owns this section.; |
| 16 | `NC_CHARTING_SECTION_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the charting section reference data. |
| 17 | `PATIENT_ID` | DOUBLE | NOT NULL | FK→ | The patient associated to the section. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `NC_CHARTED_VIEW_ID` | [NC_CHARTED_VIEW](NC_CHARTED_VIEW.md) | `NC_CHARTED_VIEW_ID` |
| `NC_CHARTING_SECTION_ID` | [NC_CHARTING_SECTION](NC_CHARTING_SECTION.md) | `NC_CHARTING_SECTION_ID` |
| `PATIENT_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [NC_CHARTED_SECTION_CE_R](NC_CHARTED_SECTION_CE_R.md) | `NC_CHARTED_SECTION_ID` |

