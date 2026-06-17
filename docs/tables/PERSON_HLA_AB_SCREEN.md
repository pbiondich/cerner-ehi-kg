# PERSON_HLA_AB_SCREEN

> Defines a person's permanent HLA antibody screen history over time.

**Description:** Person HLA Antibody Screen  
**Table type:** ACTIVITY  
**Primary key:** `HLA_AB_SCREEN_ID`  
**Columns:** 30  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | CHAR(20) |  |  | An accession number identifies an order or a group of orders. Relates the Crossmatch History to the order from which it was derived. Not populated when history is manually entered. |
| 2 | `ANTIBODY_DT_TM` | DATETIME |  |  | Date and time that the record was created. |
| 3 | `B_CELL_PRA` | DOUBLE |  |  | B-Cell percentage Panel Reactive Antibody which was derived from Antibody Screen results or entered manually into history. |
| 4 | `CHARTED_IND` | DOUBLE |  |  | Indicates whether or not a manually entered HLA antibody screen results have been sent to the OCF Clinical Event tables for charting. |
| 5 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where Antibody Screen history comments are stored. It is a foreign key reference to the primary key of the long_text table. Either derived from Antibody Screen order comments or entered manually. |
| 6 | `COMPLETE_DT_TM` | DATETIME |  |  | Date and time that the HLA antibody screen results were completed. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `DILUTION_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the dilution used in the Antibody Screen. Either derived from Antibody Screen results or entered manually into history. |
| 9 | `FLAG_IND` | DOUBLE |  |  | Indicates that the Antibody Screen has been marked (flagged) as a special or unique specimen. |
| 10 | `HLA_AB_SCREEN_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies an HLA Antibody Screen history record. |
| 11 | `MAP_SEQ_NUMBER` | DOUBLE |  |  | Reference to seq_number on the hla_ab_screen_history_map table. This records the mapping record used when creating the person_hla_ab_screen record. |
| 12 | `METHODOLOGY_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the methodology used in the Antibody Screen. Either derived from Antibody Screen results or entered manually into history. |
| 13 | `OD_RATIO_VALUE` | DOUBLE | NOT NULL |  | Holds the od ratio value for antibody screen history. |
| 14 | `OD_VALUE` | DOUBLE | NOT NULL |  | Holds the od value for antibody screen history. |
| 15 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates the Antibody Screen History to the order from which it was derived. Not populated when history is manually entered. It is a foreign key reference to the primary key of the orders table. |
| 16 | `OUTSIDE_SCREEN_IND` | DOUBLE |  |  | Indicates that the Antibody Screen was performed by an external laboratory. |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 18 | `POSSIBLE_AB_STRING` | VARCHAR(255) |  |  | Free-text sting of antibodies that might be contained in the specimen. For non-manual records this field is populated from the possible_antibodies table for the order when it is completed. |
| 19 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the user who last updated the person_hla_ab_screen record or the person who performed the testing for history which is derived from Antibody Screen results. |
| 20 | `REACTION_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the reaction of the Antibody Screen. Either derived from Antibody Screen results or entered manually into history. |
| 21 | `REMOVED_DT_TM` | DATETIME |  |  | The date and time this record was removed from HLA history. |
| 22 | `REMOVED_IND` | DOUBLE |  |  | Indicates that the record has been removed from HLA history. Records are not deleted so that a complete audit trail can be kept. |
| 23 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | The code for the specimen type used for the antibody screen. |
| 24 | `STORAGE_IND` | DOUBLE |  |  | Indicates that a specimen related to the Antibody Screen is in storage. This field is only applicable to manually entered records or those uploaded from a contributor system. |
| 25 | `T_CELL_PRA` | DOUBLE |  |  | T-Cell percentage Panel Reactive Antibody which was derived from Antibody Screen results or entered manually into history. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DILUTION_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `METHODOLOGY_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REACTION_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [HLA_SERA_QUERY_SERUM](HLA_SERA_QUERY_SERUM.md) | `HLA_AB_SCREEN_ID` |
| [HLA_XM_TRAY_WELL](HLA_XM_TRAY_WELL.md) | `HLA_AB_SCREEN_ID` |
| [HLA_XM_TRAY_WELL_SCORE](HLA_XM_TRAY_WELL_SCORE.md) | `HLA_AB_SCREEN_ID` |
| [PERSON_HLA_AB_SCN_AUDIT](PERSON_HLA_AB_SCN_AUDIT.md) | `HLA_AB_SCREEN_ID` |
| [PERSON_HLA_AB_SPEC](PERSON_HLA_AB_SPEC.md) | `HLA_AB_SCREEN_ID` |

