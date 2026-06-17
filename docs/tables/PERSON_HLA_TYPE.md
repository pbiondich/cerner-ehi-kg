# PERSON_HLA_TYPE

> Defines a person's permanent HLA type for the various HLA loci.

**Description:** Person HLA Type  
**Table type:** ACTIVITY  
**Primary key:** `HLA_TYPE_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION` | CHAR(20) |  |  | An accession number identifies an order or a group of orders. Relates the HLA Typing History to the order from which it was derived. Not populated when history is manually entered. |
| 2 | `CHARTED_IND` | DOUBLE |  |  | Indicates whether or not a manually entered HLA typing has been sent to the OCF Clinical Event tables for charting. |
| 3 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Relates this record to a specific long_text record where HLA Typing history comments are stored. It is a foreign key reference to the primary key of the long_text table. Either derived from HLA Typing order comments or entered manually. |
| 4 | `COMPLETE_DT_TM` | DATETIME |  |  | Date and time that the HLA Typing results were completed. |
| 5 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 6 | `HLA_DT_TM` | DATETIME |  |  | Date and time that the record was created. |
| 7 | `HLA_TYPE_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies an HLA Typing history record. |
| 8 | `HLA_TYPE_NOM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the nomenclature entry for the antigen which is part of the HLA Typing. Either derived from HLA Typing results or entered manually into history. |
| 9 | `LOCI_CD` | DOUBLE | NOT NULL |  | The code for the specific HLA Loci where the HLA antigen is located. Either derived from HLA Typing results or entered manually into history. |
| 10 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Relates the HLATyping History to the order from which it was derived. Not populated when history is manually entered. It is a foreign key reference to the primary key of the orders table. |
| 11 | `OUTSIDE_TYPING_IND` | DOUBLE |  |  | Indicates that the HLA Typing was performed by an external laboratory. |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 13 | `PRELIMINARY_IND` | DOUBLE |  |  | Indicates that the typing result has been performed but not verified. |
| 14 | `PRSNL_ID` | DOUBLE | NOT NULL |  | Identifies the user who last updated the person_hla_type record or the person who performed the testing for history which is derived from HLA Typing results. |
| 15 | `REFERENCE_NBR` | VARCHAR(60) | NOT NULL |  | Reference number created by ESI interface to identify duplicates. Populated with hla_type_id if not an interfaced record. |
| 16 | `REMOVED_DT_TM` | DATETIME |  |  | The date and time this record was removed from HLA history. |
| 17 | `REMOVED_IND` | DOUBLE |  |  | Indicates that the record has been removed from HLA history. Records are not deleted so that a complete audit trail can be kept. |
| 18 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL |  | The code for the specimen type used for the hla typing. |
| 19 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Relates this HLA type to an associated procedure. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HLA_TYPE_NOM_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PERSON_HLA_TYPE_AUDIT](PERSON_HLA_TYPE_AUDIT.md) | `HLA_TYPE_ID` |

