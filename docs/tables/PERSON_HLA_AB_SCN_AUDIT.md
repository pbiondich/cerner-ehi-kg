# PERSON_HLA_AB_SCN_AUDIT

> Provides an audit trail of the Person HLA Antibody Screen table whenever a record is modified.

**Description:** Person HLA Antibody Screen Audit  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBODIES` | VARCHAR(200) |  |  | A comma delimited string containing all of the antibody display values related to the codes from the person_hla_ab_spec table for to the order for which the audit trail was written. Done to save space by eliminating an audit child table. |
| 2 | `ANTIBODY_DT_TM` | DATETIME |  |  | Date and time that the original person_hla_ab_sceen record was created. |
| 3 | `AUDIT_DT_TM` | DATETIME |  |  | Date and time that the audit record was created. |
| 4 | `B_CELL_PRA` | DOUBLE |  |  | B-Cell percentage Panel Reactive Antibody. |
| 5 | `CHARTED_IND` | DOUBLE |  |  | Indicator to signify whether the row has been charted. |
| 6 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where Antibody Screen history audit trail comments are stored. It is a foreign key reference to the primary key of the long_text table. |
| 7 | `COMPLETE_DT_TM` | DATETIME |  |  | Date and time that the HLA antibody screen results were completed. |
| 8 | `DILUTION_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the dilution used in the Antibody Screen. |
| 9 | `FLAG_IND` | DOUBLE |  |  | Indicates that the Antibody Screen has been marked (flagged) as a special or unique specimen. |
| 10 | `HLA_AB_SCN_AUDIT_ID` | DOUBLE | NOT NULL |  | A sequentially assigned number which uniquely identifies an HLA Antibody Screen history audit record. |
| 11 | `HLA_AB_SCREEN_ID` | DOUBLE | NOT NULL | FK→ | Relates this audit record to the current Antibody Screen History record. It is a foreign key reference to the primary key of the person_hla_ab_screen table. |
| 12 | `METHODOLOGY_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the methodology used in the Antibody Screen. |
| 13 | `OD_RATIO_VALUE` | DOUBLE | NOT NULL |  | Holds the od ratio value for antibody screen history. |
| 14 | `OD_VALUE` | DOUBLE | NOT NULL |  | Holds the od value for antibody screen history. |
| 15 | `OUTSIDE_SCREEN_IND` | DOUBLE |  |  | Indicates that the Antibody Screen was performed by an external laboratory. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 17 | `POSSIBLE_AB_STRING` | VARCHAR(255) |  |  | Free-text string of possible antibodies entered for the order for which the audit trail was written. |
| 18 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who updated the person_hla_ab_screen record which resulted in the creation of this audit record. |
| 19 | `REACTION_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the reaction of the Antibody Screen. |
| 20 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | The code for the specimen type used for the antibody screen. |
| 21 | `STORAGE_IND` | DOUBLE |  |  | Indicates that a specimen related to the Antibody Screen is in storage. This field is only applicable to manually entered records or those uploaded from a contributor system. |
| 22 | `T_CELL_PRA` | DOUBLE |  |  | T-Cell percentage Panel Reactive Antibody. |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DILUTION_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `HLA_AB_SCREEN_ID` | [PERSON_HLA_AB_SCREEN](PERSON_HLA_AB_SCREEN.md) | `HLA_AB_SCREEN_ID` |
| `METHODOLOGY_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `REACTION_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

