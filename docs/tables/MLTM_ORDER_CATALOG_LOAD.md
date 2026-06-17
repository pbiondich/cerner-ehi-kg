# MLTM_ORDER_CATALOG_LOAD

> Table used for assisting in loading of Multum order catalog content

**Description:** Multum Order Catalog Load  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CATALOG_CKI` | VARCHAR(50) | NOT NULL |  | CKI value that corresponds to the drug level identifiers. |
| 3 | `CATALOG_CONCEPT_CKI` | VARCHAR(100) | NOT NULL |  | This column corresponds to the CONCEPT_CKI field on the Order_Catalog table. |
| 4 | `DCP_CLIN_CAT_MEAN` | VARCHAR(12) | NOT NULL |  | the clinical category of this orderable. This value will correspond to code set 16389. |
| 5 | `DESCRIPTION` | VARCHAR(255) | NOT NULL |  | the description of the orderable |
| 6 | `HIDE_IND` | DOUBLE | NOT NULL |  | Indicator whether or not to hide this synonym. |
| 7 | `MNEMONIC` | VARCHAR(255) | NOT NULL |  | The display mnemonic for the synonym. |
| 8 | `MNEMONIC_KEY_CAP` | VARCHAR(255) | NOT NULL |  | the key version of the mnemonic for this orderable. |
| 9 | `MNEMONIC_TYPE` | VARCHAR(40) | NOT NULL |  | Display value defining the type of mnemonic. |
| 10 | `MNEMONIC_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Used to identify mnemonic_type for internationalization. Expect to have a mnemonic type for each row - based on code set 6011. |
| 11 | `ORDER_ENTRY_FORMAT` | VARCHAR(50) | NOT NULL |  | The order entry format to be used by order entry applications. |
| 12 | `PRIMARY_IND` | DOUBLE | NOT NULL |  | An indicator to determine if the synonym is primary for the drug. |
| 13 | `RX_MASK_NBR` | DOUBLE | NOT NULL |  | Stores the different sub-lists the synonym belongs in, i.e. should it display with diluents, with additives, with medications, or any combination of the above. |
| 14 | `SKIP_IND` | DOUBLE | NOT NULL |  | Indicator whether to skip this row when processing. |
| 15 | `SYNONYM_CKI` | VARCHAR(50) | NOT NULL |  | CKI value that corresponds to the synonym level identifiers. |
| 16 | `SYNONYM_CONCEPT_CKI` | VARCHAR(100) | NOT NULL |  | Concept relating the specific synonym to SNOMED CT. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

