# PERSON_HLA_XM

> Defines a person's permanent HLA crossmatch history over time.

**Description:** Person HLA Crossmatch.  
**Table type:** ACTIVITY  
**Primary key:** `HLA_XM_ID`  
**Columns:** 26  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | CHAR(20) |  |  | An accession number identifies an order or a group of orders. Relates the Crossmatch History to the order from which it was derived. Not populated when history is manually entered. |
| 2 | `B_CELL_RESULT_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the B-Cell Result used in the Crossmatch. Either derived from Crossmatch results or entered manually into history. |
| 3 | `CHARTED_IND` | DOUBLE |  |  | Indicates whether or not a manually entered HLA crossmatch results have been sent to the OCF Clinical Event tables for charting. |
| 4 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where Crossmatch history comments are stored. It is a foreign key reference to the primary key of the long_text table. Either derived from Crossmatch order comments or entered manually. |
| 5 | `COMPLETE_DT_TM` | DATETIME |  |  | Date and time that the HLA crossmatch results were completed. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `DONOR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. This is the person crossmatched against this records person_id. |
| 8 | `HLA_XM_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies an HLA Crossmatch history record. |
| 9 | `HLA_XM_RES_TRAY_ID` | DOUBLE | NOT NULL | FK→ | Relates the Crossmatch History to the crossmatch result tray from which it was derived. Not populated when history is manually entered. It is a foreign key reference to the primary key of the hla_xm_res_tray table. |
| 10 | `INTERPRETATION_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where Interpretation comments are stored. It is a foreign key reference to the primary key of the long_text table. Either derived from Crossmatch orders or entered manually. |
| 11 | `MONO_CELL_RESULT_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the Monocyte Cell Result used in the Crossmatch. Either derived from Crossmatch results or entered manually into history. |
| 12 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates the Crossmatch History to the order from which it was derived. Not populated when history is manually entered. It is a foreign key reference to the primary key of the orders table. |
| 13 | `OUTSIDE_XM_IND` | DOUBLE |  |  | Indicates that the HLA Crossmatch was performed by an external laboratory. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifies the user who last updated the person_hla_xm record or the person who performed the testing for history which is derived from Crossmatch results. |
| 16 | `REMOVED_DT_TM` | DATETIME |  |  | The date and time this record was removed from HLA history. |
| 17 | `REMOVED_IND` | DOUBLE |  |  | Indicates that the record has been removed from HLA history. Records are not deleted so that a complete audit trail can be kept. |
| 18 | `TB_CELL_RESULT_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the T and B Cell result used in the Crossmatch. Either derived from Crossmatch results or entered manually into history. |
| 19 | `T_CELL_RESULT_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the T-Cell result used in the Crossmatch. Either derived from Crossmatch results or entered manually into history. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `XM_DT_TM` | DATETIME |  |  | Date and time that the record was created. |
| 26 | `XM_TYPE_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the HLA Type used in the Crossmatch. Either derived from Crossmatch results or entered manually into history. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `B_CELL_RESULT_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `DONOR_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `HLA_XM_RES_TRAY_ID` | [HLA_XM_RES_TRAY](HLA_XM_RES_TRAY.md) | `HLA_XM_RES_TRAY_ID` |
| `INTERPRETATION_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `MONO_CELL_RESULT_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TB_CELL_RESULT_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `T_CELL_RESULT_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `XM_TYPE_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_HLA_XM_AUDIT](PERSON_HLA_XM_AUDIT.md) | `HLA_XM_ID` |

