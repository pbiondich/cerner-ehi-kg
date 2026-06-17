# SN_SUP_CAB_PREF_FIELD

> Stores event code(s) to map with the supply cabinet data elements

**Description:** SN SUPPLY CABINET PREF FIELDS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_CD` | DOUBLE | NOT NULL |  | event codes for a particular document type |
| 2 | `SN_SUP_CAB_PREF_FIELD_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 3 | `SN_SUP_CAB_PREF_SEG_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the supply cabinet's segment |
| 4 | `SUP_CAB_DATA_ELM_CD` | DOUBLE | NOT NULL |  | Code of the supply cabinet data element |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SN_SUP_CAB_PREF_SEG_ID` | [SN_SUP_CAB_PREF_SEG](SN_SUP_CAB_PREF_SEG.md) | `SN_SUP_CAB_PREF_SEG_ID` |

