# OBJECT_IDENTIFIER_INDEX

> Denormalized table for Item Help

**Description:** OBJECT IDENTIFIER INDEX  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `APPROVED_IND` | DOUBLE |  |  | Indicates whether or not the item has been approved for use in the system. |
| 4 | `GENERIC_OBJECT` | DOUBLE |  |  | Holds either location_cd or class_node_id. |
| 5 | `IDENTIFIER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to identifier table. |
| 6 | `IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | Identifier type code value. |
| 7 | `ITEM_LEVEL_FLAG` | DOUBLE | NOT NULL |  | Tells whether and item is med def or not. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `LONG_PATH_TO_ITEM` | VARCHAR(200) |  |  | The classification path to the item using the description field. |
| 10 | `OBJECT_ID` | DOUBLE | NOT NULL |  | The value of the primary key of the table to which the row is related (i.e. item_id, instance_id) |
| 11 | `OBJECT_IDENTIFIER_INDEX_ID` | DOUBLE | NOT NULL |  | Primary key |
| 12 | `OBJECT_PARENT_NODE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to classification table. |
| 13 | `OBJECT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of object this row refers to (i.e. ITEM_MASTER, MED_DEF, ITEM_INSTANCE, etc.) |
| 14 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary key of the table to which the row is related (i.e. item_id, instance_id) |
| 15 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The upper case name of the table to which this row is related (i.e. ITEM_DEFINITION, ITEM_INSTANCE) |
| 16 | `PHA_TYPE_FLAG` | DOUBLE | NOT NULL |  | This flag indicates the pharmacy item type: retail or shared. |
| 17 | `PRICE_REVIEW_IND` | DOUBLE |  |  | Indicates that this vendor item has one or more prices that are in need of review. |
| 18 | `PRIMARY_IND` | DOUBLE | NOT NULL |  | Indicates if this identifier is the primary one to display for this type of identifier. |
| 19 | `PRIMARY_NBR_IND` | DOUBLE | NOT NULL |  | Indicates the primary item number to display (i.e. Stock or System Assigned) |
| 20 | `QUICKADD_IND` | DOUBLE |  |  | Indicates that the item was added through the QuickAdd application or through an interface. |
| 21 | `RELATIONSHIP_TYPE_CD` | DOUBLE | NOT NULL |  | Type of item / location relationship. |
| 22 | `REL_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The upper case name of the table to which this row is related (i.e., LOCATION,CLASS_NODE) |
| 23 | `REL_PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The upper case name of the table to which this row is related (i.e. CLASS_NODE, LOCATION) |
| 24 | `SEQUENCE` | DOUBLE |  |  | The priority of the vendor item. |
| 25 | `SHORT_PATH_TO_ITEM` | VARCHAR(200) |  |  | The classification path to the item using the short description field. |
| 26 | `SPCL_CHAR_VALUE` | VARCHAR(255) | NOT NULL |  | Stores the data except * + / and space characters in uppercase mode. |
| 27 | `SPCL_CHAR_VALUE_A_NLS` | VARCHAR(1020) | NOT NULL |  | Stores the corresponding non-English character set values for the SPCL_CHAR_VALUE column. Used to sort correctly internationally. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 33 | `VALUE` | VARCHAR(255) | NOT NULL |  | Actual value of identifier. |
| 34 | `VALUE_KEY` | VARCHAR(255) | NOT NULL |  | Uppercase value. |
| 35 | `VALUE_KEY_A_NLS` | VARCHAR(1020) |  |  | VALUE_KEY_A_NLS column |
| 36 | `VALUE_KEY_NLS` | VARCHAR(512) |  |  | Used for queries for locales other than English. |
| 37 | `VENDOR_MANF_CD` | DOUBLE | NOT NULL |  | Vendor or Manufacturer. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IDENTIFIER_ID` | [IDENTIFIER](IDENTIFIER.md) | `IDENTIFIER_ID` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `OBJECT_PARENT_NODE_ID` | [CLASS_NODE](CLASS_NODE.md) | `CLASS_NODE_ID` |

