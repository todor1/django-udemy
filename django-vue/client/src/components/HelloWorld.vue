<template>
  <div class="orders-list">
    <h2>Orders List</h2>
    <!-- <div v-if="orders.length === 0">Loading orders...</div> -->
    <ul v-for="order in orders">
      <li>
        <div>Amount: {{ order.amount }}</div>
        <div>Description: {{ order.description }}</div>
      </li>
    </ul>
    <!-- <ul v-else>
      <li v-for="order in orders" :key="order.id">
        <div>Amount: {{ order.amount }}</div>
        <div>Description: {{ order.description }}</div>
      </li>
    </ul> -->
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from "vue";
import { loadOrders } from "@/api/reporting";

export default defineComponent({
  setup() {
    const orders = ref([]);

    const addOrders = async () => {
      try {
        orders.value = await loadOrders();
        console.log("Orders loaded:", orders.value);
      } catch (error) {
        console.error("Error loading orders:", error);
      }
    };

    onMounted(() => {
      addOrders();
    });

    return {
      orders,
    };
  },
});
</script>

<style scoped lang="scss">
// .orders-list {
//   max-width: 800px;
//   margin: 0 auto;
//   padding: 20px;

//   ul {
//     list-style: none;
//     padding: 0;
//   }

//   li {
//     background: #f5f5f5;
//     margin: 10px 0;
//     padding: 15px;
//     border-radius: 4px;
//     box-shadow: 0 2px 4px rgba(0,0,0,0.1);
//   }
// }
</style>
