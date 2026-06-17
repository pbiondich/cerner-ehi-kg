# DM_CODE_SET_LOCAL

> This table holds administrative data regarding code_sets

**Description:** DM CODE SET LOCAL  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CDF_OP_IND` | DOUBLE |  |  | Preference for tool used to promote code_sets through the software factory. Does not apply at client sites. |
| 2 | `CODE_SET` | DOUBLE | NOT NULL |  | Code_set from code_value_set table |
| 3 | `CRMIMPEXP_IND` | DOUBLE |  |  | Indicates if code_set needs code_value_aliases on its code_values. |
| 4 | `CSE_OP_IND` | DOUBLE |  |  | Preference for tool used to promote code_sets through the software factory. Does not apply at client sites. |
| 5 | `CVA_OP_IND` | DOUBLE |  |  | Preference for tool used to promote code_sets through the software factory. Does not apply at client sites. |
| 6 | `CVE_OP_IND` | DOUBLE |  |  | Preference for tool used to promote code_sets through the software factory. Does not apply at client sites. |
| 7 | `CVS_OP_IND` | DOUBLE |  |  | Preference for tool used to promote code_sets through the software factory. Does not apply at client sites. |
| 8 | `CV_OP_IND` | DOUBLE |  |  | Preference for tool used to promote code_sets through the software factory. Does not apply at client sites. |
| 9 | `DESCRIPTION` | VARCHAR(60) |  |  | Description of code_set. |
| 10 | `NO_COMBINE_IND` | DOUBLE |  |  | If set to 1, DMAuthMaint will not allow code_values in this code_set to be combined. |
| 11 | `OWNER_NAME` | VARCHAR(30) |  |  | Owner of code_set. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

