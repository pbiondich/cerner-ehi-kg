# BBHIST_PRODUCT

> This activity table is a smaller version of the Product table, and is intended to store products loaded in from previous systems. It will also be used in the future to store purged products from thelive inventory.(from the Product table).

**Description:** Blood Bank Historical Product  
**Table type:** ACTIVITY  
**Primary key:** `PRODUCT_ID`  
**Columns:** 34  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABO_CD` | DOUBLE | NOT NULL |  | This number represents the ABO blood group of the product, ex. "O", "A", etc. This column will be empty for derivative products. |
| 2 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 6 | `ALTERNATE_NBR` | VARCHAR(20) |  |  | This column can be used to record the original number labeled on the bag of blood, in the case of sites who choose to re-number blood products received from their supplier. This way they can still track the product by its original number, which is important in the for look-backs. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `CROSS_REFERENCE` | VARCHAR(40) |  |  | This column is a free-text one that allows a history upload to fill this column with some value that cross-references it to a record on the previous system for the same blood product or derivative. In the case of HNA Classic as the previous system, the unique unit number from the Blood Inventory file (BI01-unit-nbr1) would be in this column. |
| 9 | `DONOR_XREF_TXT` | VARCHAR(40) | NOT NULL |  | This is a free-text column that allows a donor history upload to populate this column with a cross-reference value that uniquely identifies the donor in the previous contributor system. |
| 10 | `EXPIRE_DT_TM` | DATETIME | NOT NULL |  | Defines the date/time when the product expired. |
| 11 | `FLAG_CHARS` | CHAR(2) |  |  | Stores the flag characters of an uploaded ISBT- 128 donation number. The flag characters are used to convey specific information other than the unique identification of the product. The three provided types of flag characters represent process control (with ISBT 128-defined meaning), process control (with a local blood center-defined meaning), or data transmission check. |
| 12 | `INV_AREA_CD` | DOUBLE | NOT NULL |  | Identifies the code value for the current inventory area where the product resides. This inventory area is any area that keeps blood products or derivatives in an inventory, from which the products are dispensed. This means that the it could be the main blood bank, or a surgical area or emergency room that stocks blood for use in surgery. This column is optional, ex. in the case of sites with only one blood bank on the system. |
| 13 | `MODIFIED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | This column represents the PRODUCT_ID of the original product from which this product was created through product modification. The product_id is the primary key of the BBHIST_PRODUCT table. It is an internal system-assigned number that uniquely identifies a product in the blood bank. |
| 14 | `MODIFIED_PRODUCT_IND` | DOUBLE |  |  | Indicates whether the product has been modified after it was received into the blood bank's inventory. This indicator is only updated on the "parent" product, not the new "child" products created from the original parent product. |
| 15 | `OWNER_AREA_CD` | DOUBLE | NOT NULL |  | Identifies the code value for the blood bank owner area where the product resided. This owner area is a fully-functioning blood bank that is responsible for the blood received or drawn there. A blood bank owner area can have several inventory areas within it. An example of an owner area would be "General Hospital North", with its inventory areas being "Main BB - GH North", "Surgery - GH North", and "ER - GH North" |
| 16 | `POOLED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | This column represents the PRODUCT_ID of the new pooled product into which this product was pooled through the pooling process. The product_id is the primary key of the BBHIST_PRODUCT table. It is an internal system-assigned number that uniquely identifies a product in the blood bank. |
| 17 | `POOLED_PRODUCT_IND` | DOUBLE |  |  | Indicates whether the product is a pooled product, i.e.., a product that was created through the pooling process. This indicator should only exist on the newly created product, not the products that were components within the pool. |
| 18 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | The type of product (ex. "Fresh Frozen Plasma") which was on the label of the bag of blood. |
| 19 | `PRODUCT_CLASS_CD` | DOUBLE | NOT NULL |  | The class of products to which this specific type of product belongs. Two classes of products may be used: blood products and derivatives. |
| 20 | `PRODUCT_ID` | DOUBLE | NOT NULL | PK | An internal system-assigned number that ensures the uniqueness of every row on this table. |
| 21 | `PRODUCT_NBR` | VARCHAR(20) | NOT NULL |  | The number assigned to this product to identify it. Also known as "unit number". It is the number that is on the bag of blood products to identify it. In the case of derivative products, it is the lot number from the batch of derivatives. |
| 22 | `PRODUCT_NBR_FORMAT_CD` | DOUBLE | NOT NULL |  | Stores the uploaded product's number format (ISBT, Eurocode, None, etc.) |
| 23 | `PRODUCT_SUB_NBR` | CHAR(5) |  |  | A letter or number assigned to each product with the same product number, in order to make them unique. An example is splitting red blood cells into smaller bags of red cells. The sub number is assigned as "1", "2", "3", etc. or as "A", "B", "C", etc. |
| 24 | `RH_CD` | DOUBLE | NOT NULL |  | The code value which represents the Rh for this blood product (ex. "Pos", "Neg"). This column will be empty for derivative products. |
| 25 | `SUPPLIER_ID` | DOUBLE | NOT NULL | FK→ | This column represents an organization_ID, which is the primary key to the ORGANIZATION table. It is an internal system-assigned number. It identifies the supplier of this product, the organization who sent the product to the transfusion service, ex. "American Red Cross". |
| 26 | `SUPPLIER_PREFIX` | CHAR(5) |  |  | This column may be empty. It represents the FDA originating supplier prefix on this bag of blood, i.e., the donor center where the blood was originally drawn from the blood donor. An example is "09", which becomes part of the product number, e.g., "09G12345". |
| 27 | `UNIT_MEAS_CD` | DOUBLE | NOT NULL |  | The unit of measure in which this product's volume was recorded, ex. "ML". |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 33 | `UPLOAD_DT_TM` | DATETIME | NOT NULL |  | The date and time the history product upload occurred. |
| 34 | `VOLUME` | DOUBLE |  |  | Indicates the final volume for this blood product at the time it was disposed of. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODIFIED_PRODUCT_ID` | [BBHIST_PRODUCT](BBHIST_PRODUCT.md) | `PRODUCT_ID` |
| `POOLED_PRODUCT_ID` | [BBHIST_PRODUCT](BBHIST_PRODUCT.md) | `PRODUCT_ID` |
| `SUPPLIER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [BBHIST_PRODUCT](BBHIST_PRODUCT.md) | `MODIFIED_PRODUCT_ID` |
| [BBHIST_PRODUCT](BBHIST_PRODUCT.md) | `POOLED_PRODUCT_ID` |
| [PRODUCT_NOTE](PRODUCT_NOTE.md) | `BBHIST_PRODUCT_ID` |

