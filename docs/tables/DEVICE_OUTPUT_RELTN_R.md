# DEVICE_OUTPUT_RELTN_R

> This table will relate items like Organizations and Event Sets to specified Device Output Relationships.

**Description:** Device Output Relation Relationships  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEVICE_OUTPUT_RELTN_ID` | DOUBLE | NOT NULL | FK→ | A Foreign Key that defines a relationship to devices which can also be tied to Organizations and Event Set Codes |
| 2 | `DEVICE_OUTPUT_RELTN_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY. |
| 3 | `EVENT_SET_CD` | DOUBLE | NOT NULL |  | Event Set Code that can be used as part of the relationship between devices and output_content types |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key to Organization table. Used to route organizations to devices through a relationship with event sets |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEVICE_OUTPUT_RELTN_ID` | [DEVICE_OUTPUT_RELTN](DEVICE_OUTPUT_RELTN.md) | `DEVICE_OUTPUT_RELTN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

