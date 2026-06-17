# SN_RPT_FIELD_REF

> Contains the reference information for each field in a report section. This information includes the key, default display, and various other indicators.

**Description:** SN_RPT_FIELD_REF  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY` | VARCHAR(60) | NOT NULL |  | The default display value for this field. |
| 2 | `FIELD_KEY` | VARCHAR(20) | NOT NULL |  | The unique field key for this field. These keys are set by the SurgiNet engineering team and are used in various scripts to determine what data to retrieve for this field. |
| 3 | `FIELD_SIZE` | DOUBLE | NOT NULL |  | The default number of columns that this field uses. |
| 4 | `LINE_IND` | DOUBLE | NOT NULL |  | Determines if a '____' can be used as the value for this field. |
| 5 | `MULTI_SETTING_FLAG` | DOUBLE | NOT NULL |  | Determines the type of setting selection that can be made for this field. |
| 6 | `RPT_FIELD_GRP_CD` | DOUBLE | NOT NULL |  | Determines what field group this field belongs in. |
| 7 | `RPT_FIELD_REF_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 8 | `RPT_SECT_REF_ID` | DOUBLE | NOT NULL | FK→ | A foreign key into the SN_RPT_SECT_REF table to determine what section this field belongs in. |
| 9 | `SCRIPT_NAME` | VARCHAR(32) | NOT NULL |  | Determines which script the values for this field are derived from. |
| 10 | `SETTING_IND` | DOUBLE | NOT NULL |  | Determines if this field contains additional field settings. |
| 11 | `SIZABLE_IND` | DOUBLE | NOT NULL |  | Determines if the size of this field is adjustable by the user. |
| 12 | `SORTABLE_IND` | DOUBLE | NOT NULL |  | Determines if the user can sort on this field or not. |
| 13 | `STACKABLE_IND` | DOUBLE | NOT NULL |  | Determines if this field can be stacked on top of another field. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RPT_SECT_REF_ID` | [SN_RPT_SECT_REF](SN_RPT_SECT_REF.md) | `RPT_SECT_REF_ID` |

