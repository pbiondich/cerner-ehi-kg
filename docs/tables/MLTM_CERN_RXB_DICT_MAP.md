# MLTM_CERN_RXB_DICT_MAP

> Mapping of Dictionary ID's to Code CKI's

**Description:** RxBuilder Dictionary Map  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CODE_CKI` | VARCHAR(255) | NOT NULL |  | Code CKI - Cerner CKI |
| 2 | `CODE_SET` | DOUBLE | NOT NULL |  | The values for CODE_SET will come from the CSV file that will load the table. These correspond to the code_set values on the code_value table. |
| 3 | `DESCRIPTION` | VARCHAR(255) | NOT NULL |  | Short description |
| 4 | `DICTIONARY_ID` | DOUBLE | NOT NULL |  | Multum Dictionary ID from mltm_rxb_dictionary table |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

