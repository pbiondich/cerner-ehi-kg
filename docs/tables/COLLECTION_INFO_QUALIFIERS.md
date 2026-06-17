# COLLECTION_INFO_QUALIFIERS

> This is where all of the collection requirements are stored.

**Description:** Collection Info Qualifiers  
**Table type:** REFERENCE  
**Primary key:** `CATALOG_CD`, `SEQUENCE`, `SPECIMEN_TYPE_CD`  
**Columns:** 25  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_LABELS` | DOUBLE |  |  | The number of extra labels which will be printed for orders with these collection requirements. The additional labels will not be assigned to a container. |
| 2 | `AGE_FROM_MINUTES` | DOUBLE |  |  | The beginning patient age in minutes for the age range associated with the collection requirements. |
| 3 | `AGE_TO_MINUTES` | DOUBLE |  |  | The ending patient age in minutes at which the collection requirements will no longer be applied. The collection requirements are applicable for patients whose ages are greater than or equal to the Age From Minutes, and less than the Age To Minutes. |
| 4 | `ALIQUOT_IND` | DOUBLE |  |  | An indicator that aliquot container requirements are associated with the collection requirements. |
| 5 | `ALIQUOT_ROUTE_SEQUENCE` | DOUBLE |  |  | Not currently used. |
| 6 | `ALIQUOT_SEQ` | DOUBLE | NOT NULL |  | This field will contain the sequence value of the parent container's collection requirements when aliquot container requirements exist. It is used to read all associate aliquot requirements on the aliquot_info_qualifers table directly for a given coll_info_seq value. If no aliquots exist, the field will contain a value of 0.0. |
| 7 | `CATALOG_CD` | DOUBLE | NOT NULL | PK | The internal number assigned by the system to the order catalog item associated with the collection requirements. |
| 8 | `COLLECTION_PRIORITY_CD` | DOUBLE | NOT NULL |  | Provides the ability to flex collection requirements by priority. |
| 9 | `COLL_CLASS_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Collection Class associated with the collection requirements. |
| 10 | `MIN_VOL` | DOUBLE |  |  | The numeric value which, along with the Minimum Volume Units, defines the smallest amount of specimen needed for the collection requirements. |
| 11 | `MIN_VOL_UNITS` | CHAR(15) |  |  | The units associated with the Minimum Volume numeric value. |
| 12 | `OPTIONAL_IND` | DOUBLE |  |  | An indicator that the collection requirements are acceptable for the order catalog item, but are not the preferred requirements. Not in use at this time. |
| 13 | `REQUIRED_IND` | DOUBLE |  |  | Not currently used. |
| 14 | `SEQUENCE` | DOUBLE | NOT NULL | PK | The numeric value assigned by the system to indicate the sequence or position of each row of collection requirements. |
| 15 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Service Resource associated with the collection requirements. |
| 16 | `SPECIES_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Species associated with the collection requirements. Not currently used. |
| 17 | `SPECIMEN_TYPE_CD` | DOUBLE | NOT NULL | PK | The internal number assigned by the system to the Specimen Type associated with the collection requirements. |
| 18 | `SPEC_CNTNR_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Specimen Container associated with the collection requirements. |
| 19 | `SPEC_HNDL_CD` | DOUBLE | NOT NULL |  | The internal number assigned by the system to the Special Handling Comments associated with the collection requirements. |
| 20 | `UNITS_CD` | DOUBLE | NOT NULL |  | Not in use at this time. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (9)

| From table | Column |
|------------|--------|
| [ALT_COLLECTION_INFO](ALT_COLLECTION_INFO.md) | `CATALOG_CD` |
| [ALT_COLLECTION_INFO](ALT_COLLECTION_INFO.md) | `COLL_INFO_SEQ` |
| [ALT_COLLECTION_INFO](ALT_COLLECTION_INFO.md) | `SPECIMEN_TYPE_CD` |
| [COLLECTION_INFO_QUAL_HIST](COLLECTION_INFO_QUAL_HIST.md) | `CATALOG_CD` |
| [COLLECTION_INFO_QUAL_HIST](COLLECTION_INFO_QUAL_HIST.md) | `COLL_INFO_SEQ` |
| [COLLECTION_INFO_QUAL_HIST](COLLECTION_INFO_QUAL_HIST.md) | `SPECIMEN_TYPE_CD` |
| [LAB_HANDLING](LAB_HANDLING.md) | `CATALOG_CD` |
| [LAB_HANDLING](LAB_HANDLING.md) | `COLL_INFO_SEQ` |
| [LAB_HANDLING](LAB_HANDLING.md) | `SPECIMEN_TYPE_CD` |

