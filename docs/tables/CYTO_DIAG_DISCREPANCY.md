# CYTO_DIAG_DISCREPANCY

> This reference table contains the variance and discrepancy designations assigned to combinations of initial screening diagnoses compared to the verification diagnoses for a gynecologic cytology report. These associations are based on alpha responses.

**Description:** Cytology Diagnosis Discrepancy  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `HCFA_FLAG` | DOUBLE |  |  | This field is not used at this time. |
| 2 | `INTERNAL_FLAG` | DOUBLE |  |  | This field contains a numeric flag value documenting the comparison relationship (discrepancy or variance, for example) for the two alpha response (nomenclature) values included in the table entry. |
| 3 | `NOMENCLATURE_X_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the X-axis alpha response (nomenclature) codes included in the comparison pair included as part of the table key. The internal ID code could be used to join to the NOMENCLATURE table. |
| 4 | `NOMENCLATURE_Y_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the Y-axis alpha response (nomenclature) codes included in the comparison pair included as part of the table key. The internal ID code could be used to join to the NOMENCLATURE table. |
| 5 | `REFERENCE_RANGE_FACTOR_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the table storing the reference range (alpha response values, in this example) information for the diagnosis alpha response report component. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOMENCLATURE_X_ID` | [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `NOMENCLATURE_ID` |
| `NOMENCLATURE_Y_ID` | [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `NOMENCLATURE_ID` |
| `REFERENCE_RANGE_FACTOR_ID` | [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `REFERENCE_RANGE_FACTOR_ID` |
| `REFERENCE_RANGE_FACTOR_ID` | [ALPHA_RESPONSES](ALPHA_RESPONSES.md) | `REFERENCE_RANGE_FACTOR_ID` |

