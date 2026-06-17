# MIC_ABNORMAL_LIST

> This table associates the abnormal report responses with the procedure/source/service resource combination defined on the mic_abn_org_response_code table.

**Description:** Microbiology Abnormal Organisms and Responses  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_CD` | DOUBLE | NOT NULL |  | This field identifies the code value of the report response that is defined as abnormal for the procedure/source/service resource. Abnormal results can be organisms or coded responses. |
| 2 | `CRITERIA_ID` | DOUBLE | NOT NULL | FK→ | This field identifies the unique value for each set of abnormal results defined for a procedure/source/service resource combination defined on the mic_abn_org_response_code table. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CRITERIA_ID` | [MIC_ABN_ORG_RESPONSE_CODE](MIC_ABN_ORG_RESPONSE_CODE.md) | `CRITERIA_ID` |

