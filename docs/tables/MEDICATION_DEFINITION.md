# MEDICATION_DEFINITION

> The parent table for items stored within the formulary.

**Description:** Medication definition  
**Table type:** REFERENCE  
**Primary key:** `ITEM_ID`  
**Columns:** 46  
**Referenced by:** 23 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALTERNATE_DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | The category used for grouping this product, when ordered in a partial unit, on fill lists and batches for continuous dispensing. This will be defaulted from the form_dispense_cat_r table entries for this item's form. |
| 2 | `ALWAYS_DISPENSE_FROM_FLAG` | DOUBLE |  |  | This field helps to indicate where this product is dispensed from. |
| 3 | `CKI` | VARCHAR(255) |  |  | Cerner Knowledge Index field for Multum MMDC numbers. Syntax is "MUL.FRMLTN! " |
| 4 | `COMMENT1_ID` | DOUBLE | NOT NULL | FK→ | Link to long_text table for the first order note. |
| 5 | `COMMENT1_TYPE` | DOUBLE |  |  | Type of Order comment #1 |
| 6 | `COMMENT2_ID` | DOUBLE | NOT NULL |  | Key to long_text table for second order entry note. |
| 7 | `COMMENT2_TYPE` | DOUBLE |  |  | Type of second order entry comment |
| 8 | `COMPOUND_TEXT_ID` | DOUBLE | NOT NULL |  | Key to long_text table for compounding instructions. |
| 9 | `CONTINUOUS_FILTER_IND` | DOUBLE |  |  | Indicates whether this product should be displayed when entering a continuous IV order |
| 10 | `DEFAULT_PAR_DOSES` | DOUBLE |  |  | The default par which overrides any default par value from the frequency schedule. e.g.: PRN bulk item is ordered Q4H. The default par value from the frequency schedule is 6, but for bulk items it should be only 1. |
| 11 | `DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | The category used for grouping this product, when ordered as a whole unit, on fill lists and batches for continuous dispensing. This will be defaulted from the form_dispense_cat_r table entries for this item's form. |
| 12 | `DISPENSE_QTY` | DOUBLE | NOT NULL |  | The number of units of a pharmacy product that you should dispense for the ordered dose |
| 13 | `DISPENSE_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | Values from PHA_GET_PHARMUNIT or code set 54 |
| 14 | `DIVISIBLE_IND` | DOUBLE |  |  | Defines whether this product can be split, broken, etc. To create a dose. The divisible is defaulted from the form.divisible. |
| 15 | `FORMULARY_STATUS_CD` | DOUBLE | NOT NULL |  | Defines the acceptance of this product by the institution. |
| 16 | `FORM_CD` | DOUBLE | NOT NULL |  | The dosage form of the product. |
| 17 | `GIVEN_STRENGTH` | VARCHAR(25) |  |  | Strength of the product as retrieved from the drug database. |
| 18 | `INTERMITTENT_FILTER_IND` | DOUBLE |  |  | Indicates whether this item is selectable when building in Intermittent IV. |
| 19 | `INV_MASTER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the Inventory item which QOH is tracked, in place of the formulary item. This is an FK column from table ITEM_DEFINITION. |
| 20 | `ITEM_ID` | DOUBLE | NOT NULL | PK FK→ | Item id inherited from item_master |
| 21 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | The legal status of the drug as assigned by the governing body. |
| 22 | `MAX_PAR_SUPPLY` | DOUBLE |  |  | For a singe dispense event of this item as PRN, the maximum number of units to supply. Mostly, this will be used by multiple-day fill lists, eg, a long-term care facility. |
| 23 | `MDX_GFC_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Nomenclature id for the Micromedex identifier for this product s generic formulation, including active ingredients, strength and dosage form. |
| 24 | `MED_FILTER_IND` | DOUBLE |  |  | Indicates whether this item is selectable when building a medication order. |
| 25 | `MED_TYPE_FLAG` | DOUBLE |  |  | Indicates the type of this formulation. |
| 26 | `MEQ_FACTOR` | DOUBLE |  |  | strength/volume ratio expressed in millequivalents |
| 27 | `MMOL_FACTOR` | DOUBLE |  |  | strength/volume ratio expressed in millimoles. |
| 28 | `OE_FORMAT_FLAG` | DOUBLE |  |  | Preferred order format for this item |
| 29 | `ORDER_ALERT1_CD` | DOUBLE | NOT NULL | FK→ | First order alert code for this item. |
| 30 | `ORDER_ALERT2_CD` | DOUBLE | NOT NULL | FK→ | Second order alert code for this item. |
| 31 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 32 | `PARENT_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the parent formulary item that the child item is grouped to. This is an FK column from table ITEM_DEFINITION. |
| 33 | `PREMIX_IND` | DOUBLE | NOT NULL |  | Indicates whether the medication product is a premix containing multiple ingredients. |
| 34 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Link to price schedule for this item. |
| 35 | `PRIMARY_MANF_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Link to the manufacturer item that is currently being dispensed. |
| 36 | `SIDE_EFFECT_CODE` | VARCHAR(10) |  |  | Side effect code (used for printing on MARs) |
| 37 | `STRENGTH` | DOUBLE |  |  | Strength of the product used to determine the available products to dispense based upon the requested dose. |
| 38 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measurement associated with the Strength. |
| 39 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 40 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 41 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 42 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 43 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 44 | `USED_AS_BASE_IND` | DOUBLE |  |  | Indicates whether this product can be ordered as a base solution. NOTE: This helps the OE application determine whether to prompt the user whether the order is continuous or intermittent, i.e., whether or not an infusion rate is necessary. Domain: 0 = never, 1 = sometimes, 2 = always domain: never = 0 sometimes = 1 always = 2 0 = Always 1 = Sometimes 2 = Never |
| 45 | `VOLUME` | DOUBLE |  |  | Volume of the product used to determine the available products to dispense based upon the requested dose. |
| 46 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measurement associated with the volume. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT1_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `INV_MASTER_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `MDX_GFC_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORDER_ALERT1_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ORDER_ALERT2_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PARENT_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |
| `PRIMARY_MANF_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |

## Referenced by (23)

| From table | Column |
|------------|--------|
| [CE_MED_ADMIN_IDENT](CE_MED_ADMIN_IDENT.md) | `ITEM_ID` |
| [DISPENSE_REPLACE_AUDIT](DISPENSE_REPLACE_AUDIT.md) | `REPLACE_ITEM_ID` |
| [MED_DEF_FLEX](MED_DEF_FLEX.md) | `ITEM_ID` |
| [MED_DEF_LOC_R](MED_DEF_LOC_R.md) | `MED_DEF_ITEM_ID` |
| [MED_IDENTIFIER](MED_IDENTIFIER.md) | `ITEM_ID` |
| [ORDER_THERAP_SBSTTN](ORDER_THERAP_SBSTTN.md) | `ITEM_ID` |
| [RXA_MED_COPAY_TIER_HX](RXA_MED_COPAY_TIER_HX.md) | `ITEM_ID` |
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `MED_ITEM_ID` |
| [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `MED_ITEM_ID` |
| [RXS_LOC_ENCNTR_INVENTORY](RXS_LOC_ENCNTR_INVENTORY.md) | `ITEM_ID` |
| [RX_EXT_DRUG_ITEM_AUDIT](RX_EXT_DRUG_ITEM_AUDIT.md) | `ITEM_ID` |
| [RX_EXT_ITEM_UPDATE_AUDIT](RX_EXT_ITEM_UPDATE_AUDIT.md) | `ITEM_ID` |
| [RX_EXT_ORD_PRD_SYNC_AUDIT](RX_EXT_ORD_PRD_SYNC_AUDIT.md) | `ITEM_ID` |
| [RX_EXT_ORD_PRD_SYNC_AUDIT](RX_EXT_ORD_PRD_SYNC_AUDIT.md) | `NEW_ITEM_ID` |
| [RX_MED_ORD_DETAIL](RX_MED_ORD_DETAIL.md) | `ITEM_ID` |
| [RX_PRODUCT_ASSIGN_AUDIT](RX_PRODUCT_ASSIGN_AUDIT.md) | `ITEM_ID` |
| [RX_PRODUCT_ASSIGN_AUDIT](RX_PRODUCT_ASSIGN_AUDIT.md) | `SET_ITEM_ID` |
| [RX_PRODUCT_CHANGE_NOTE](RX_PRODUCT_CHANGE_NOTE.md) | `ITEM_ID` |
| [RX_THERAP_SBSTTN_FROM](RX_THERAP_SBSTTN_FROM.md) | `FROM_ITEM_ID` |
| [RX_THERAP_SBSTTN_TO](RX_THERAP_SBSTTN_TO.md) | `TO_ITEM_ID` |
| [RX_WORKFLOW_STS](RX_WORKFLOW_STS.md) | `ITEM_ID` |
| [RX_WORKFLOW_STS_ITEM](RX_WORKFLOW_STS_ITEM.md) | `ITEM_ID` |
| [SYNONYM_ITEM_R](SYNONYM_ITEM_R.md) | `ITEM_ID` |

