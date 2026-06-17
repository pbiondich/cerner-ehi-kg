# IMPLANT_HISTORY

> Contains information about the alert set for the rule

**Description:** IMPLANT HISTORY  
**Table type:** ACTIVITY  
**Primary key:** `IMPLANT_HISTORY_ID`  
**Columns:** 50  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BIOLOGICAL_IMP_SRC_CD` | DOUBLE | NOT NULL |  | Indicates the Biological source of an implant mfr catalog item |
| 3 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | Site of the Implanted Item |
| 4 | `DEVICE_IDENTIFIER_TXT` | VARCHAR(50) |  |  | The Device Identifier (if any) for the implanted item. This would be the unique_id from a scanned barcode. |
| 5 | `DONOR_NUMBER_TXT` | VARCHAR(255) |  |  | Textt field which contains the donor number |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter Id of the person |
| 7 | `EXPIRATION_DT_TM` | DATETIME |  |  | Indicates the item expire date time |
| 8 | `EXPLANT_DT_TM` | DATETIME |  |  | Explanted Date |
| 9 | `EXPLANT_DT_TM_PREC_FLAG` | DOUBLE | NOT NULL |  | Precision of date/time: 0=precise to time, 1=precise to day, 2=precise to month, 3=precise to year |
| 10 | `EXPLANT_REASON_CD` | DOUBLE | NOT NULL |  | Explanted Reason |
| 11 | `GMDN_PT_NAME` | VARCHAR(4000) |  |  | Indicates the "Global Medical Device Nomenclature Preferred Term" name of the implant item. |
| 12 | `IMPLANTED_DT_TM` | DATETIME |  |  | Indicates the Implanted date time |
| 13 | `IMPLANTED_DT_TM_PREC_FLAG` | DOUBLE | NOT NULL |  | Precision of date/time: 0=precise to time, 1=precise to day, 2=precise to month, 3=precise to year |
| 14 | `IMPLANTED_FACILITY_CD` | DOUBLE | NOT NULL |  | Location Type defines the kind of location (i.e., nurse unit, room, inventory location, etc.). Location types have Cerner defined meanings in the common data foundation |
| 15 | `IMPLANTED_FACILITY_FT` | VARCHAR(255) |  |  | Location as free text value |
| 16 | `IMPLANTED_PRSNL_FT` | VARCHAR(255) |  |  | The Provider name as free text value who implanted the Item |
| 17 | `IMPLANTED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Provider who implanted the Item |
| 18 | `IMPLANTED_QUANTITY` | DOUBLE | NOT NULL |  | The quantity of the items Implanted |
| 19 | `IMPLANT_DATA_SOURCE_CD` | DOUBLE | NOT NULL |  | Data Source of the Implant Item |
| 20 | `IMPLANT_HISTORY_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 21 | `IMPLANT_INSTANCE_GRP_ID` | DOUBLE | NOT NULL |  | Group Implants for audit history |
| 22 | `IMPLANT_INSTANCE_SEQ` | DOUBLE | NOT NULL |  | Sequencing of Implants |
| 23 | `IMPLANT_ITEM_FT` | VARCHAR(255) |  |  | Item identifier as free text value |
| 24 | `IMPLANT_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Indicates the associated item identifier in ITEM_MASTER table |
| 25 | `IMPLANT_TYPE_CD` | DOUBLE | NOT NULL |  | Implanted Implant Type |
| 26 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the long text identifier |
| 27 | `LOT_NUMBER_TXT` | VARCHAR(255) |  |  | Lot Number of an added item |
| 28 | `MANUFACTURED_DT_TM` | DATETIME |  |  | Manufactured date of an implanted item |
| 29 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | Manufacturer code of an item |
| 30 | `MANUFACTURER_FT` | VARCHAR(255) |  |  | The manufacturer name as free text value |
| 31 | `MANUFACTURER_MODEL_NBR_TXT` | VARCHAR(255) |  |  | The manufacturer model number text |
| 32 | `MR_CLASSIFICATION_CD` | DOUBLE | NOT NULL |  | Manufacturer MR classification of an Item |
| 33 | `NON_BIOLOGICAL_IMP_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the Non-Biologic Implant type of an implant mfr catalog item |
| 34 | `ORIGINATING_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Indicates the "Originating Encounter ID" for implant item added in Implant History Tab. |
| 35 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Used to Store the identifier of the parent table named in PARENT_ENTITY_NAME |
| 36 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Used to Store the name of the parent Table for the ID value in PARENT_ENTITY_ID |
| 37 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person_id of the person from the person table for whom Implant is being added |
| 38 | `PROCEDURE_CD` | DOUBLE | NOT NULL |  | Scheduled Surgical Procedure Code |
| 39 | `PROCEDURE_FT` | VARCHAR(255) |  |  | Scheduled Surgical Procedure Name |
| 40 | `PROCEDURE_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Codified value of the Procedure Nomenclature against which Implant item has been documented. |
| 41 | `SERIAL_NUMBER_TXT` | VARCHAR(255) |  |  | Serial and Donor Number |
| 42 | `SNOMEDCT_DESCRIPTION` | VARCHAR(255) |  |  | An association between a human-readable phrase(term) and a particular SNOMED CT concept. |
| 43 | `SNOMED_IDENTIFIER` | DOUBLE | NOT NULL |  | A unique integer identifier applied to each SNOMED CT component (Concept, Description, or Relationship) |
| 44 | `SURG_CASE_PROC_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the procedure documented in the surgical case |
| 45 | `UDI_TXT` | VARCHAR(255) |  |  | Unique device identifier,This would be a numeric value representing a bar coded unique identifier for each instance of an item |
| 46 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `IMPLANTED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `IMPLANT_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORIGINATING_ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROCEDURE_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `SURG_CASE_PROC_ID` | [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SURG_CASE_PROC_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [IMPLANT_HISTORY_MATERIAL](IMPLANT_HISTORY_MATERIAL.md) | `IMPLANT_HISTORY_ID` |
| [IMPLANT_HISTORY_REVIEW](IMPLANT_HISTORY_REVIEW.md) | `IMPLANT_HISTORY_ID` |

