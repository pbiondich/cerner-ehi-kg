# PL_INSURANCE_DEFAULTS

> This table stores the configuration of the insurance fields based on insurance companies.

**Description:** This table stores the configuration of the insurance fields based on ins co  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_LABEL` | CHAR(30) |  |  | Customized label for this field and insurance combination. |
| 2 | `FIELD_CD` | DOUBLE | NOT NULL |  | Insurance field that is being customized. |
| 3 | `FIELD_TYPE_FLAG` | DOUBLE |  |  | Indicates the type of insurance field being customized. |
| 4 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organizatgion id is the key to the table, which identifies the insurance organization for which these defaults will be used. |
| 5 | `PL_INSURANCE_DEFAULTS_ID` | DOUBLE | NOT NULL |  | Unique identifier for each row on the table. |
| 6 | `REQUIRED_IND` | DOUBLE |  |  | Indicates whether the insurance field should be required or not. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

