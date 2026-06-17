# SN_RPT_FIELD_SETTING

> Contains additional information for a field in the SN_RPT_FIELD table.

**Description:** SN RPT FIELD SETTING  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was initially inserted. |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that created the row. |
| 5 | `PRIMARY_ENTITY_ID` | DOUBLE | NOT NULL |  | The _id that corresponds to this settings primary id. This is commonly used for fields that require additional information to get the actual value for the report. For example: segment comments would require a primary_entity_id equal to the seg_cd which corresponds to the segment that we are wanting to get the comments for. |
| 6 | `PRIMARY_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the table that the primary_entity_id corresponds to. |
| 7 | `RPT_FIELD_ID` | DOUBLE | NOT NULL | FK→ | The field that these settings belong to. |
| 8 | `RPT_FIELD_SETTING_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 9 | `SECONDARY_ENTITY_ID` | DOUBLE | NOT NULL |  | The _id that corresponds to this settings secondary id. This is commonly used for fields that require additional information beyond a single id to get the actual value for the report. For example: A DTA off of a form would require two event_cd's to retrieve the value out of the clinical events; a form level event_cd and a control level event_cd. |
| 10 | `SECONDARY_ENTITY_NAME` | VARCHAR(32) |  |  | The name of the table that the secondary_entity_id corresponds to. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RPT_FIELD_ID` | [SN_RPT_FIELD](SN_RPT_FIELD.md) | `RPT_FIELD_ID` |

