# PERSON_HLA_XM_AUDIT

> Provides an audit trail of the Person HLA Crossmatch table whenever a record is modified.

**Description:** Person HLA Crossmatch Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUDIT_DT_TM` | DATETIME |  |  | Date and time that the audit record was created. |
| 2 | `B_CELL_RESULT_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the B-Cell result which is part of the HLA Crossmatch. |
| 3 | `CHARTED_IND` | DOUBLE |  |  | Indicator to signify whether the row has been charted. |
| 4 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where HLA Crossmatch history audit trail comments are stored. It is a foreign key reference to the primary key of the long_text table. |
| 5 | `COMPLETE_DT_TM` | DATETIME |  |  | Date and time that the HLA crossmatch results were completed. |
| 6 | `DONOR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. This is the person crossmatched against this records person_id. |
| 7 | `HLA_XM_AUDIT_ID` | DOUBLE | NOT NULL |  | A sequentially assigned number which uniquely identifies an HLA Crossmatch Audit history record. |
| 8 | `HLA_XM_ID` | DOUBLE | NOT NULL | FK→ | Relates this audit record to the current HLA Crossmatch History record. It is a foreign key reference to the primary key of the person_hla_xm table. |
| 9 | `INTERPRETATION_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where Interpretation comments are stored. It is a foreign key reference to the primary key of the long_text table. Either derived from Crossmatch orders or entered manually. |
| 10 | `MONO_CELL_RESULT_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the Monocyte cell result which is part of the HLA Crossmatch. |
| 11 | `OUTSIDE_XM_IND` | DOUBLE |  |  | Indicates that the HLA Crossmatch was performed by an external laboratory. |
| 12 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who updated the person_hla_xm record which resulted in the creation of this audit record. |
| 13 | `TB_CELL_RESULT_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the T and B cell result which is part of the HLA Crossmatch. |
| 14 | `T_CELL_RESULT_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the T-Cell result which is part of the HLA Crossmatch. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 20 | `XM_DT_TM` | DATETIME |  |  | Date and time that the original person_hla_xm record was created. |
| 21 | `XM_TYPE_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the Crossmatch Type which is part of the HLA Crossmatch. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `B_CELL_RESULT_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DONOR_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `HLA_XM_ID` | [PERSON_HLA_XM](PERSON_HLA_XM.md) | `HLA_XM_ID` |
| `INTERPRETATION_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `MONO_CELL_RESULT_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TB_CELL_RESULT_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `T_CELL_RESULT_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `XM_TYPE_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

