# PCS_CHARGE_MOD_ABN

> This table tracks charges which have met their charge points and their ABN status has been modified in PathNet.

**Description:** PathNet Common Services Charge Modification ABN  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AS_OF_DT_TM` | DATETIME | NOT NULL |  | The date and time that the charges ABN status changed. |
| 2 | `CHARGE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the charge used to references the Charge table. |
| 3 | `CHARGE_MOD_ABN_ID` | DOUBLE | NOT NULL |  | This field is the unique identifier for the PCS_CHARGE_MOD_ABN. |
| 4 | `CHARGE_STATUS_CD` | DOUBLE | NOT NULL |  | The code for the status of the charge. |
| 5 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The encounters organization at the time the ABN was modified for this charge. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHARGE_ITEM_ID` | [CHARGE](CHARGE.md) | `CHARGE_ITEM_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

