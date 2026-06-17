# HD_D_GUARANTOR_TYPE

> The guarantor type indicates that the guarantor for the encounter is either a person or an organization. This code is used to determine which set of tables to query to find the guarantor.

**Description:** HD_D_GUARANTOR_TYPE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GUARANTOR_TYPE_DESC` | VARCHAR(100) | NOT NULL |  | The long description for the guarantor type indicating the guarantor for the encounter. |
| 2 | `GUARANTOR_TYPE_ID` | DOUBLE | NOT NULL |  | IDENTIFIER |
| 3 | `GUARANTOR_TYPE_NAME` | VARCHAR(40) | NOT NULL |  | The PHINVADs concept code for the Person Relationship or same as desc field if there isn't a standard code. |
| 4 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 5 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 6 | `UPDT_USER` | VARCHAR(40) |  |  | The user that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

